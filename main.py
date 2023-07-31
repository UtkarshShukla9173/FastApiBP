import os

import uvicorn
from app.main import app

# app = create_app()

# comment
if __name__ == "__main__":
    uvicorn.run("__main__:app", port=int(os.environ.get("PORT", 8080)), host="0.0.0.0", reload=True)
    # "__main__:app" required for when config.reload or config.workers > 1 on heroku