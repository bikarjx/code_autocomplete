from script_auto_complete.operators.extend_word_operators import get_extend_word_operators
from script_auto_complete.operators.insert_template_operators import get_insert_template_operators
from script_auto_complete.operators.api_context_operators import get_api_context_operators
from script_auto_complete.operators.suggestions_from_before import get_suggestion_from_text_before

def get_text_operators():
    operators = []
    operators.extend(get_insert_template_operators())
    operators.extend(get_suggestion_from_text_before())
    operators.extend(get_api_context_operators())
    operators.extend(get_extend_word_operators())
    return operators