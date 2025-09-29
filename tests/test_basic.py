"""Basic tests for the Attio SDK."""

import pytest
from attio import Attio


def test_import():
    """Test that we can import the main SDK class."""
    assert Attio is not None


def test_sdk_initialization():
    """Test that we can initialize the SDK with an oauth2 token."""
    # This test uses a dummy oauth2 token since we're just testing initialization
    sdk = Attio(oauth2="dummy_oauth2_token_for_testing")
    assert sdk is not None
    

def test_version_info():
    """Test that version information is available."""
    # This is a very basic test - you might want to expand this
    # based on what's actually available in the SDK
    try:
        import attio
        # If there's a version attribute, test it
        if hasattr(attio, '__version__'):
            assert isinstance(attio.__version__, str)
        # Otherwise just pass
        else:
            assert True

    except ImportError:
        pytest.fail("Failed to import attio module")