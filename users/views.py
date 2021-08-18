from django.shortcuts import redirect, render

from users.forms import ProfileRegistrationForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        user_form = ProfileRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = ProfileRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    form = ProfileUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)
