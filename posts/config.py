class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://lmalhoit:7Lauren10@localhost:5432/posts"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://lmalhoit:7Lauren10@localhost:5432/posts-test"
    DEBUG = True
