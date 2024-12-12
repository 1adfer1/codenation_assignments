from flask import render_template, Blueprint, request
from fav_bands import favourite_bands

my_view = Blueprint("my_view", __name__)

class BandEntry():
    def __init__(self, song_name, song_album, song_artist, song_rating):
        self.song = song_name
        self.album = song_album
        self.artist = song_artist
        self.rating = song_rating

bands=[]

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html", bands= bands)

@my_view.route("/page3", methods=["GET", "POST"])
def page3():
    if request.method == "POST":
        new_band = BandEntry(
            request.form["added_song"],
            request.form["added_album"],
            request.form["added_artist"],
            request.form["added_rating"])
        bands.append(new_band)
    return render_template("page3.html")

# @my_view.route("/page4", methods=["GET", "POST"])
# def page4():
#     if request.method == "POST":
#         filter_num = int(request.form["added_rating"])
#         filter_bands = [band for band in bands if band.rating==filter_num]
#     return render_template("page4.html", bands = filter_bands)
