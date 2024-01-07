from django.shortcuts import render


# ============== ERRORS HANDLER ==============|
def error_404(request, exception):
    '''fungsi menampilkan template error 404'''
    return render(request, 'ppdb/404.html')

def error_505(request, exception):
    '''fungsi menampilkan template error 505'''
    return render(request, 'ppdb/505.html')