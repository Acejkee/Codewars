def get_size(w,h,d):
    volume = w*h*d
    area = (2*w*h)+(2*w*d)+(2*h*d)
    return [area , volume]