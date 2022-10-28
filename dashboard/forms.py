from django import forms
from dashboard.models import FeedBack

class FeedBackForm(forms.ModelForm):
	# text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
	# rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = FeedBack
		fields = ('name','email','feedback','suggestion')