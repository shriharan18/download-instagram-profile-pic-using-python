# This code was written by Shreeharan for the YouTube Channel Stark Intelligence
import instaloader  # importing the module

mod = instaloader.Instaloader()

user = input("Enter your Instagram username: ")     # getting the user name from the user

mod.download_profile(user, profile_pic_only=True)   # downloading the profile picture
