from django.shortcuts import render

def home(request):
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=023A7EA8-C5FB-413B-A941-8F371330C182
    import requests
    import json

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=023A7EA8-C5FB-413B-A941-8F371330C182")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ..."
        if api[0]['Category']['Name'] == "Good":
            category_description = "description Good"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "description Moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "description USG"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "description Unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "VeryUnhealthy":
            category_description = "description veryunhealthy"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "description hazardous"
            category_color = "hazardous"

        return render(request, 'home.html',
                      {'api': api, 'category_description': category_description, 'category_color': category_color})

    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=023A7EA8-C5FB-413B-A941-8F371330C182")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ..."
        if api[0]['Category']['Name'] == "Good":
            category_description = "description Good"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "description Moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "description USG"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "description Unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "VeryUnhealthy":
            category_description = "description veryunhealthy"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "description hazardous"
            category_color = "hazardous"

        return render(request, 'home.html',
                      {'api': api, 'category_description': category_description, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})