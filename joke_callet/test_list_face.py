import os

def get_current_dir():
    file_dir=os.path.dirname(os.path.abspath(__file__))
    # print("当前目录：",file_dir)
    return file_dir

def get_face_dir():

    face_dir=os.path.join(get_current_dir(),"faces")
    # print("表情目录：",face_dir)
    return face_dir
def get_video_dir():
    face_dir=os.path.join(get_current_dir(),"videos")
    # print("表情目录：",face_dir)
    return face_dir
def get_faces_list():
    faces_list=os.listdir(get_face_dir())
    # print("表情列表：",faces_list)
    return [ os.path.join(get_face_dir(),i) for i in faces_list]

def get_videos_list():
    faces_list=os.listdir(get_video_dir())
    # print("表情列表：",faces_list)
    return [ os.path.join(get_video_dir(),i) for i in faces_list]
# a=get_faces_list()
# print(a)

