from django.shortcuts import render, redirect
from .models import URL
from .forms import URLForm
from django.views import View


class RedirectURL(View):
    def get(self, request, short_url):
        url = URL.objects.get(short_url=short_url)
        return redirect(url.long_url)


class ShortenURLView(View):
    def get(self, request):
        form = URLForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('long_url')
            try:
                shortened = URL.objects.get(long_url=url)
            except URL.DoesNotExist:
                shortened = URL.objects.create(long_url=url)
                shortened.save()
            return render(request, 'shortened_url.html', {'shortened': shortened})
        else:
            return render(request, 'index.html', {'form': form})
