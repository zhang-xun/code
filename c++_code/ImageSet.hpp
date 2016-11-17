//
//  ImageSet.hpp
//  learn_opencv
//
//  Created by zhangxun on 16/8/24.
//  Copyright © 2016年 zx. All rights reserved.
//

#ifndef ImageSet_hpp
#define ImageSet_hpp

#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>


#include <iostream>
#include <vector>
#include <string>

using namespace std;

class ImageSet
{
public:
    ImageSet(string);
    
    vector<string> getFiles();
    
    int getFileSize();
    
    string getDirPath();
    
    
private:
    vector<string> filelist;
    int fileNumber;
    string path;
    
};

#endif /* ImageSet_hpp */
