from django.http import HttpResponseForbidden
import re

class BotDetectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of common bot user-agents
        bot_user_agents = ['bot', 'crawl', 'spider', 'slurp', 'wget', 'curl', 'facebook', 'googlebot', 'bingbot']
        
        # Get the User-Agent header
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

        # Check if user-agent matches any bot signatures
        if any(bot in user_agent for bot in bot_user_agents):
            return HttpResponseForbidden("Access Denied: Bot detected!")
        
        # Continue with the request processing
        response = self.get_response(request)
        return response
