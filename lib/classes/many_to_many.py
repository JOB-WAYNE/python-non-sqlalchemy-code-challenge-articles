class Article:
    def __init__(self, author: 'Author', magazine: 'Magazine', title: str):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        
        self._title = title
        self.author = author
        self.magazine = magazine

    @property
    def title(self):
        return self._title
    
    @property
    def author(self) -> 'Author':
        return self._author

    @author.setter
    def author(self, author: 'Author'):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author.")
        self._author = author

    @property
    def magazine(self) -> 'Magazine':
        return self._magazine

    @magazine.setter
    def magazine(self, magazine: 'Magazine'):
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine.")
        self._magazine = magazine


class Author:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = name
        self._articles = []  # Initialize the list of articles

    @property
    def name(self) -> str:
        return self._name

    def add_article(self, article: Article):
        if isinstance(article, Article) and article not in self._articles:
            self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        # Placeholder method for further implementation
        pass


class Magazine:
    def __init__(self, name: str, category: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        
        self._name = name
        self._category = category
        self._articles = []  # Initialize the list of articles

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def add_article(self, article: Article):
        if isinstance(article, Article) and article not in self._articles:
            self._articles.append(article)

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return self.contributors()
