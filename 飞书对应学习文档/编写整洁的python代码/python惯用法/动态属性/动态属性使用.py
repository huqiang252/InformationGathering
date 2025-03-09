

class DynamicAttributes:

    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute {attr}"
        )



if __name__ == '__main__':
    dyn = DynamicAttributes("value")
    print(dyn.attribute) #value
    print(dyn.fallback_something)  #[fallback resolved] something
    # print(dyn.non_existent)     #AttributeError: DynamicAttributes has no attribute non_existent

    dyn.__dict__['fallback_new'] = 'new_value' #修改属性
    print(dyn.fallback_new)  #new_value


    print(getattr(dyn, 'not_something', 'default')) #default
