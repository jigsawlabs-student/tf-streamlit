

from app import create_app, db
from app.models import Position, Scraping
from app.settings import db_conn
from app.setup import seed_positions_from_csv, seed_scrapings_from_csv

app = create_app(db_conn)

@app.cli.command("init-db")
def init_db_command():
    """Create database tables and seed data."""
    db.create_all()

@app.cli.command("seed-db")
def seed_db():
    scraping_count = db.session.query(Scraping).count()
    position_count = db.session.query(Position).count()
    print(f"Will seed if scrapings and positions is over zero, currently there are \n {scraping_count} scrapings and \n {position_count} positions ")
    if not scraping_count:
        seed_scrapings_from_csv('./data/scrapings.csv')
    if not position_count:
        seed_positions_from_csv('./data/positions.csv')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Position': Position, 'Scraping': Scraping}

