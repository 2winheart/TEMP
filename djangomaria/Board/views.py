from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board
from .forms import BoardForm

def Board_main(request):
	listA = Board.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'Board/Board_main.html', {'listA': listA})

def Board_detail(request,pk):
	listB = Board.objects.get(id=pk)
	return render(request, 'Board/Board_detail.html', {'listB': listB})

def Board_create(request):
	if request.method == 'POST':
		form = BoardForm(request.POST)
		if form.is_valid():
			Board = form.save(commit=False)
			Board.created_date = timezone.now()
			Board.save()
		return redirect('Board_detail', pk=Board.pk)
	else:
		form = BoardForm()
	return render(request, 'Board/Board_create.html', {'form': form})

def Board_edit(request, pk):
	listC = Board.objects.get(id=pk)
	if request.method == 'POST':
		form = BoardForm(request.POST, instance=listC)
		if form.is_valid():
			listC = form.save(commit=False)
			listC.created_date = timezone.now()
			listC.save()
		return redirect('Board_detail', pk=listC.pk)
	else:
		form = BoardForm(instance=listC)
	return render(request, 'Board/Board_edit.html', {'form': form})

def Board_delete(request, pk):
	p = Board.objects.get(id=pk)
	p.delete();
	return render(request, 'Board/Board_delete.html')
