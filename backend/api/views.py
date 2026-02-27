from rest_framework.decorators import api_view
from rest_framework.response import Response
import time


@api_view(['GET'])
def health_check(request):
    """Simple health check endpoint to verify API is working."""
    return Response({'status': 'healthy', 'message': 'Django API is running!'})


# Mock AI responses for different topics
AI_RESPONSES = {
    'crut_what': {
        'messageType': 'longAnswer',
        'title': 'What Is a Charitable Remainder Unitrust (CRUT)?',
        'content': 'A Charitable Remainder Unitrust is an irrevocable trust that converts appreciated assets into a variable lifetime income stream, while providing an upfront charitable tax deduction. After the trust term ends, the remaining assets go to a designated charity.',
        'howItWorks': [
            'You contribute appreciated assets to the trust.',
            'The trust sells the assets without immediate capital gains tax.',
            'You receive annual income based on a fixed percentage of the trust\'s value.',
            'At the end of the trust term, the remaining assets transfer to charity.'
        ],
        'actions': ['Set up a call with us', 'Check if it is right for me']
    },
    'crut_positive': {
        'messageType': 'tablePositive',
        'title': 'A CRUT is advised for your investment strategy!',
        'content': '',
        'savings': '$12,000 per year',
        'tableData': {
            'headers': ['With CRUT', 'Without CRUT'],
            'rows': [
                {'label': 'Tax Liability', 'values': ['$12,000/year', '$24,000/year'], 'highlight': True},
                {'label': 'Charity Amount', 'values': ['$10,000/year', '$0']},
                {'label': 'Savings', 'values': ['$12,000/year', '$0'], 'highlight': True}
            ]
        },
        'howToSetup': 'You can book a call with us to know more and we will set it up for you!',
        'actions': ['View Best Options for me', 'I need to re-enter my asset details', 'How is this calculated?', 'Set up a call with us']
    },
    'crut_negative': {
        'messageType': 'tableNegative',
        'title': 'A CRUT is NOT advised for your investment strategy!',
        'content': 'A CRUT will not have any effect in your portfolio. You can however look at other strategies like solar projects to save on taxes!',
        'tableData': {
            'headers': ['With CRUT', 'Without CRUT'],
            'rows': [
                {'label': 'Tax Liability', 'values': ['$24,000/year', '$24,000/year']},
                {'label': 'Charity Amount', 'values': ['$0', '$0']},
                {'label': 'Savings', 'values': ['$0', '$0']}
            ]
        },
        'actions': ['How is this calculated?', 'What other investments can I pursue?', 'I need to re-enter my asset details', 'Set up a call with us to know other options']
    },
    'default': {
        'messageType': 'text',
        'title': '',
        'content': 'Based on your profile and financial goals, I can help you explore various investment strategies that might be suitable for your situation. Would you like me to analyze any specific aspect of your investment strategy?',
        'actions': ['View recommendations', 'Schedule consultation']
    }
}


@api_view(['POST'])
def ai_chat(request):
    """Handle AI chat messages and return appropriate responses."""
    message = request.data.get('message', '').lower()
    
    # Simulate thinking time
    time.sleep(1)
    
    # Determine which response to return based on keywords
    if 'analyze crut viability' in message or 'asset value' in message:
        # Form submission - return positive recommendation for demo
        response_data = AI_RESPONSES['crut_positive']
    elif 'what is' in message and ('crut' in message or 'charitable remainder' in message):
        response_data = AI_RESPONSES['crut_what']
    elif ('fit' in message or 'correct' in message or 'right' in message or 'strategy' in message) and ('crut' in message or 'charitable' in message):
        # Randomly choose between positive and negative for demo
        import random
        response_data = AI_RESPONSES['crut_positive'] if random.random() > 0.3 else AI_RESPONSES['crut_negative']
    elif 'crut' in message or 'charitable remainder' in message:
        response_data = AI_RESPONSES['crut_what']
    else:
        response_data = AI_RESPONSES['default']
    
    return Response({
        'response': response_data['content'],
        'messageType': response_data.get('messageType', 'text'),
        'title': response_data.get('title', ''),
        'subtitle': response_data.get('subtitle', ''),
        'actions': response_data.get('actions', []),
        'tableData': response_data.get('tableData'),
        'howItWorks': response_data.get('howItWorks'),
        'howToSetup': response_data.get('howToSetup'),
        'savings': response_data.get('savings')
    })
