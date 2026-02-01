"""
Entity Extraction Processor

This module handles entity extraction from documents and images using Claude API.
Uses Claude's vision capabilities for image processing.

Updated: February 2026
"""

import os
import json
import base64
from typing import Dict, Any, Union
from PIL import Image
import io

from anthropic import Anthropic

# Default model for entity extraction (vision-capable)
DEFAULT_MODEL = "claude-3-5-haiku-20241022"


def _get_anthropic_client() -> Anthropic:
    """Get Anthropic client"""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")

    if not api_key:
        raise ValueError("No API key configured. Please set ANTHROPIC_API_KEY environment variable.")

    return Anthropic(api_key=api_key)


def extract_entities(document_content: Union[str, bytes], custom_instructions: str, is_image: bool = False) -> Dict[str, Any]:
    """
    Extract named entities from text or images using Claude API.
    If `is_image` is True, process the content as an image.

    Args:
        document_content: Text content or image bytes
        custom_instructions: Additional instructions for extraction
        is_image: Whether the content is an image

    Returns:
        Dictionary with extracted entities
    """
    try:
        client = _get_anthropic_client()
    except ValueError as e:
        return {"error": str(e), "entities": []}

    # JSON format for response
    json_format = """
    {
        "entities": [
            {
                "type": "PERSON/COMPANY NAME/COMPANY UEN/DOCUMENT DATE/NRIC",
                "value": "extracted entity",
                "context": "relevant surrounding text"
            }
        ]
    }
    """

    system_prompt = f"""Task: Named Entity Extraction
Instructions: {custom_instructions}

Analyze the following document and extract named entities.
**STRICTLY return only JSON** in this format:
```json
{json_format}
```
Do not include any explanations, bullet points, or markdown formatting.
Exclude any mentions of Tertiary Infotech as the company."""

    try:
        # Handle image content
        if is_image and isinstance(document_content, bytes):
            # Convert bytes to base64 for API
            base64_image = base64.b64encode(document_content).decode('utf-8')

            # Use Claude vision for image processing
            response = client.messages.create(
                model=DEFAULT_MODEL,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": system_prompt},
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": base64_image
                                }
                            }
                        ]
                    }
                ]
            )
        elif isinstance(document_content, Image.Image):
            # Handle PIL Image objects
            buffer = io.BytesIO()
            document_content.save(buffer, format='PNG')
            base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

            response = client.messages.create(
                model=DEFAULT_MODEL,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": system_prompt},
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": base64_image
                                }
                            }
                        ]
                    }
                ]
            )
        else:
            # Handle text content
            response = client.messages.create(
                model=DEFAULT_MODEL,
                max_tokens=4096,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": str(document_content)}
                ]
            )

        # Parse response
        response_text = response.content[0].text.strip()

        # Clean up markdown if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        response_text = response_text.strip()

        # Parse JSON
        extracted_entities = json.loads(response_text)

        # Validate structure
        if not isinstance(extracted_entities, dict) or "entities" not in extracted_entities:
            return {"entities": [], "error": "Invalid JSON format"}

        return extracted_entities

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return {"entities": [], "error": "Invalid JSON response"}
    except Exception as e:
        print(f"Error extracting entities: {e}")
        return {"entities": [], "error": str(e)}
