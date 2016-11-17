
//
//  ImageSet.cpp
//  learn_opencv
//
//  Created by zhangxun on 16/8/24.
//  Copyright © 2016年 zx. All rights reserved.
//

#include "ImageSet.hpp"


ImageSet::ImageSet(string s)
{
    path = s;
    
    DIR * dir;
    struct dirent* dirp;
    
    if((dir=opendir(path.c_str()))==NULL)
    {
        cout << "can not open" << s << endl;
        exit(0);
    }
    
    while( (dirp = readdir(dir) ) != NULL)
    {
        string temp = string(dirp->d_name);
        if(dirp->d_type == 8)
        {
            if(temp.find(".BMP") < temp.length() ||
               temp.find(".Jpeg") < temp.length() ||
               temp.find(".png") < temp.length() ||
               temp.find(".jpg") < temp.length())
            {
                //cout << "find image" << temp << endl;
                filelist.push_back(temp);
            }
        }
    }
    
    fileNumber = (int)filelist.size();
    
}



vector<string> ImageSet::getFiles( )
{
   
    return filelist;
    
}

int ImageSet::getFileSize()
{
    return fileNumber;
}

string ImageSet::getDirPath()
{
    return path;
}