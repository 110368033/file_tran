close all;
clear;

f= fopen('Chrisy_LH_X_up_1_ch1.dat'); %改成要轉的檔案檔名
data=fread(f,'float32');
fclose(f);

data_1= data(1:2:end);
data_2= data(2:2:end);

IQ1=data_1+i*data_2;

IQ=abs(IQ1);
% IQ_output=IQ(1:12500:end); %可以設定要間隔多少取一點，目前是6000000/12500=480筆

figure;plot(IQ); %全部的點都畫出來，但是圖片會跑久一點
% figure;plot(IQ); %畫波形，不要的話可以註解掉

% csvwrite('C:\filename.csv',IQ_output); %可以設定路徑和存檔檔名


% dname = uigetdir('C:\');
% disp(dname);
% 
% str=[dname,dname];
% filepathandname=join(str,"-");
% disp(filepathandname);


