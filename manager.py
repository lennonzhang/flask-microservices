from project import create_app, db
from flask_script import Manager
import unittest

app = create_app()
manager = Manager(app)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()

