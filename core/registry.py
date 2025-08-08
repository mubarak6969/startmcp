class ModelRegistry:
    _registry = {}

    @classmethod
    def register(cls, model, permissions=None):
        cls._registry[model.__name__] = {
            'model': model,
            'permissions': permissions or {}
        }

    @classmethod
    def get_all_models(cls):
        return cls._registry
