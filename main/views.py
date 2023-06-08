from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
import json

from .forms import ContractForm
from .models import Contract


@staff_member_required
def main(request):
    contracts = Contract.objects.all()
    for contract in contracts:
        contract.calculate_end_date()
    return render(request, "main/index.html", {"contracts": contracts})


@staff_member_required
@csrf_exempt
def create_contract(request):
    if request.method == "POST":
        form = ContractForm(json.load(request))
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            contract.calculate_end_date()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"errors": form.errors})
