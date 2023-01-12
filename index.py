
import imageio

from weathers.Weather import weather_data
from weathers.fog import add_fog
from weathers.rain import add_rain
from weathers.snow import add_snow

# Import Image
input_img = imageio.imread_v2('./static/home_img.jpg')
# Weather Conditions
temp, time, sky, other_data = weather_data("Canada")
print("Weather Desc :", sky)
print("Time in Hrs:", time)
print("Temperature :", temp)

weather = ["snow", "rain", "fog"]
forecast = sky.lower()
for w in weather:
    if w in forecast:
        if w == "snow":
            add_snow(input_img, 140)
        elif w == "rain":  # Rain effect for both day and night
            if (time > 6) and (time <= 19):
                add_rain(input_img, 0.9)
            elif (time > 19) or (time <= 6):
                add_rain(input_img, 0.2)
        elif w == "fog":
            add_fog(input_img)
