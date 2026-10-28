"""Backward-compatible imports for the ScamShield detection engine."""

from scamshield.ai.detector import analyze_content, analyze_media_file, analyze_url, is_phishing

__all__ = ["analyze_content", "analyze_media_file", "analyze_url", "is_phishing"]
