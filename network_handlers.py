from playwright.sync_api import Page

def handle_network_errors(page: Page):
    """Listens for network errors and handles them."""

    def on_response(response):
        if response.status >= 400:
            print(f"Request failed: {response.url} with status {response.status}")

    def on_request_failed(request):
        print(f"Request failed: {request.url} with failure reason: {request.failure}")

    page.on("response", on_response)
    page.on("requestfailed", on_request_failed)
