"""Bridge.py. The main Python-(Swift) plugin bundle entry module"""
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("Loaded python bundle")