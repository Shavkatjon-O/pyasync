from pyasync.applications import Pyasync

app = Pyasync()


@app.route("/")
async def home(scope, receive, send):
    return await app.render(
        template_name="index.html",
        context={
            "title": "Home",
            "name": "Shavkatjon",
        },
    )


@app.route("/about")
async def about(scope, receive, send):
    return "About page"


@app.route("/contact")
async def contact(scope, receive, send):
    return "Contact page"
