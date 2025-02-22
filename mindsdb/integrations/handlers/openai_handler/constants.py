OPENAI_API_BASE = 'https://api.openai.com/v1'

CHAT_MODELS = ('gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-instruct', 'gpt-4', 'gpt-4-32k')
COMPLETION_MODELS = ('babbage-002', 'davinci-002')
FINETUNING_MODELS = ('gpt-3.5-turbo', 'babbage-002', 'davinci-002')
COMPLETION_LEGACY_BASE_MODELS = ('davinci', 'curie', 'babbage', 'ada')

FINETUNING_LEGACY_MODELS = COMPLETION_LEGACY_BASE_MODELS
COMPLETION_LEGACY_MODELS = COMPLETION_LEGACY_BASE_MODELS + \
                        tuple(f'text-{model}-001' for model in COMPLETION_LEGACY_BASE_MODELS) + \
                        ('text-davinci-002', 'text-davinci-003')

EMBEDDING_MODELS = ('text-embedding-ada-002',) + \
                tuple(f'text-similarity-{model}-001' for model in COMPLETION_LEGACY_BASE_MODELS) + \
                tuple(f'text-search-{model}-query-001' for model in COMPLETION_LEGACY_BASE_MODELS) + \
                tuple(f'text-search-{model}-doc-001' for model in COMPLETION_LEGACY_BASE_MODELS) + \
                tuple(f'code-search-{model}-text-001' for model in COMPLETION_LEGACY_BASE_MODELS) + \
                tuple(f'code-search-{model}-code-001' for model in COMPLETION_LEGACY_BASE_MODELS)

ALL_MODELS = list(set(CHAT_MODELS + COMPLETION_MODELS + COMPLETION_LEGACY_MODELS + EMBEDDING_MODELS))  # noqa