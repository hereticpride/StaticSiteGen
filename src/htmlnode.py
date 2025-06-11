class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
        if self.children == None:
            self.children = []
        if self.props == None:
            self.props = {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = " "
        if self.props == {}:
            return ""
        for key, value in self.props.items():
            result += f'{key}="{value}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("leaf node has no value")
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag, value, None, props)

    def to_html(self):
        props_str = ""

        if self.value == None:
            raise ValueError("leaf node has no value")
        elif self.tag == None:
            return self.value
        else:
            if self.props != None:
                for key, val in self.props.items():
                    props_str += f' {key}="{val}"'
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children == None:
            raise ValueError("ParentNode children property cannot be None")
        
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode had no tag property")
        elif self.children == None:
            raise ValueError("ParentNode has no children")
        elif not self.children:
            raise ValueError("Children is an empty list. ParentNode must have atleast (1) child")
        else:
            result = ""
            for child in self.children:
                recur_child = child.to_html()
                result += recur_child
            return f"<{self.tag}>{result}</{self.tag}>"