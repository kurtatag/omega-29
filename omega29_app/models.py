from .extensions import db


class TreeNodeType(db.Model):
    __tablename__ = 'tree_node_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<TreeNodeType: '{self.name}'>"


class TreeNode(db.Model):
    __tablename__ = 'tree_node'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    endpoint = db.Column(db.String(50), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('tree_node_type.id'),
        nullable=False)
    type = db.relationship('TreeNodeType',
        backref=db.backref('nodes', lazy=True))
    parent_id = db.Column(db.Integer, db.ForeignKey('tree_node.id'),
        nullable=True, default=None)
    parent = db.relationship('TreeNode', remote_side=[id],
        backref='child_nodes')

    def __repr__(self):
        return f"<{self.type.name}: '{self.name}'>"


class PageComponentType(db.Model):
    __tablename__ = 'page_component_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<PageComponentType: '{self.name}'>"


class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Language: '{self.name}'>"


class PageComponent(db.Model):
    __tablename__ = 'page_component'
    id = db.Column(db.Integer, primary_key=True)
    page_section_number = db.Column(db.Integer, nullable=False)
    order_number = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('tree_node.id'),
        nullable=False)
    page = db.relationship('TreeNode',
        backref=db.backref('components', lazy=True))
    page_component_type_id = db.Column(db.Integer,
        db.ForeignKey('page_component_type.id'), nullable=False)
    page_component_type = db.relationship('PageComponentType',
        backref=db.backref('components', lazy=True))
    language_id = db.Column(db.Integer,
        db.ForeignKey('language.id'), nullable=True, default=None)
    language = db.relationship('Language',
        backref=db.backref('components', lazy=True))

    def __repr__(self):
        return f"<PageComponent {self.page_component_type.name}: " \
               f"'{self.content[:10]}'>"
