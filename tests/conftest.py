"""Pytest fixtures for atlassian-page-client tests."""

import pytest
import json
from unittest.mock import Mock


@pytest.fixture
def sample_page_data():
    """Sample Atlassian page data for testing."""
    return {
        "id": "12345",
        "title": "Test Page",
        "type": "page",
        "status": "current",
        "body": {
            "storage": {
                "value": "<p>Test content</p><table ac:local-id='test-table'><tr><td>Cell 1</td></tr></table>",
                "representation": "storage"
            }
        },
        "version": {
            "number": 1,
            "_links": {
                "self": "https://example.atlassian.net/wiki/rest/api/content/12345/version/1"
            }
        },
        "_links": {
            "self": "https://example.atlassian.net/wiki/rest/api/content/12345"
        }
    }


@pytest.fixture
def sample_html_content():
    """Sample HTML content for testing."""
    return """
    <div class="wiki-content">
        <p>Test paragraph</p>
        <table ac:local-id="test-table">
            <tr>
                <td>Cell 1</td>
                <td>Cell 2</td>
            </tr>
        </table>
        <div data-test="test-div">Test div</div>
    </div>
    """


@pytest.fixture
def mock_requests_response():
    """Mock requests response."""
    response = Mock()
    response.status_code = 200
    response.url = "https://example.atlassian.net/api/test"
    return response


@pytest.fixture
def client_config():
    """Configuration for AtlassianPageClient."""
    return {
        "email": "test@example.com",
        "token": "test_token_123",
        "base_url": "https://example.atlassian.net"
    }
