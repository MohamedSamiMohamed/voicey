[y2, fs2] = audioread ("output2.wav");
if (size(y2,2)==2)
y2= (y2(:,1)+y2(:,2))/2;
endif

#---------------------------------------
[y3, fs3] = audioread ("output3.wav");
if (size(y3,2)==2)
y3= (y3(:,1)+y3(:,2))/2;
endif

#---------------------------------------
[y4, fs4] = audioread ("output4.wav");
if (size(y4,2)==2)
y4= (y4(:,1)+y4(:,2))/2;
endif

min_shape=size(y3,1);



#function read_audio(path)
#  [y2, fs2] = audioread (path);
 # disp(size(y2,2));
  
  #if (size(y2,2)==2)
   # y2= (y2(:,1)+y2(:,2))/2;
  #endif
#endfunction



[y, fs] = read_audio("output2.wav")
