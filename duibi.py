import wx
  
class MyPanel(wx.Panel):  
    def __init__(self, parent, id):  
        wx.Panel.__init__(self, parent, id)  
        image_file = 'C:\\Users\\Administrator\\Desktop\\beijing.jpg'  
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 25))  
        image_width = to_bmp_image.GetWidth()  
        image_height = to_bmp_image.GetHeight()  
        set_title = u'相似视频快速甄别检索软件'
        parent.SetTitle(set_title)
        textbotton = wx.StaticText(self.bitmap,-1,u'北京非斗数据科技发展有限公司',pos=(320,460))

        #创建一个按钮  
        text1 = wx.StaticText(self.bitmap,-1,u'请导入原始视频：',pos=(110,110))
        self.path1 = wx.TextCtrl(self.bitmap,-1,'',pos=(110,130),size=(250,25))
        self.button1 = wx.Button(self.bitmap,-1,u'打开文件',pos=(365,128))
        
        text2 = wx.StaticText(self.bitmap,-1,u'请导入待甄别视频：',pos=(110,170))
        self.path2 = wx.TextCtrl(self.bitmap,-1,'',pos=(110,190),size=(250,25))
        self.button2 = wx.Button(self.bitmap,-1,u'打开文件',pos=(365,188))

        text3 = wx.StaticText(self.bitmap,-1,u'请导入原始视频：',pos=(110,300))
        self.path3 = wx.TextCtrl(self.bitmap,-1,'',pos=(110,320),size=(250,25))
        self.button3 = wx.Button(self.bitmap,-1,u'打开文件',pos=(365,318))

        text4 = wx.StaticText(self.bitmap,-1,u'请导入待甄别视频所在文件夹：',pos=(110,360))
        self.path4 = wx.TextCtrl(self.bitmap,-1,'',pos=(110,380),size=(250,25))
        self.button4 = wx.Button(self.bitmap,-1,u'选择文件夹',pos=(365,378))

        lblist = [u'单视频甄别','批量甄别']
        self.rbox = wx.RadioBox(self.bitmap,-1,u'请选择工作模式',pos=(550,95),choices = lblist)
        text5 = wx.StaticText(self.bitmap,-1,u'输出路径：',pos=(552,160))
        self.path5 = wx.TextCtrl(self.bitmap,-1,'',pos=(550,180),size=(180,25))
        self.button5 = wx.Button(self.bitmap,-1,u'选择路径',pos=(550,205))
        
        self.button_start =wx.Button(self.bitmap,-1,u'开始',pos=(600,320),size=(100,50))

        self.bitmap.Bind(wx.EVT_BUTTON,self.Inputpath,self.button4)
        self.bitmap.Bind(wx.EVT_BUTTON,self.dakaiwenjian,self.button1)
        self.bitmap.Bind(wx.EVT_BUTTON,self.dakaiwenjian1,self.button2)
        self.bitmap.Bind(wx.EVT_BUTTON,self.dakaiwenjian2,self.button3)
        self.bitmap.Bind(wx.EVT_BUTTON,self.Inputpath1,self.button5)
        self.bitmap.Bind(wx.EVT_BUTTON,self.loading123,self.button_start)
    def Inputpath(self,event):

        dlg = wx.DirDialog(self,u'选择视频路径',style=wx.DD_DEFAULT_STYLE)

        if dlg.ShowModal() == wx.ID_OK:

            path_ = dlg.GetPath()


            self.path4.SetValue('%s' % path_)

            dlg.Destroy()
    def Inputpath1(self,event):

        dlg = wx.DirDialog(self,u'选择输出路径',style=wx.DD_DEFAULT_STYLE)

        if dlg.ShowModal() == wx.ID_OK:

            path_ = dlg.GetPath()


            self.path5.SetValue('%s' % path_)

            dlg.Destroy()
    def loading123(self,event):
        dlg =wx.MessageDialog(self,u'系统正在处理中……',u'Loading...')
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            overdlg =wx.MessageDialog(self,u'处理完成，甄别结果已存入目标文件夹','甄别完成')
            if overdlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
    def dakaiwenjian(self,event):
            filesFilter = u"视频文件(*.avi)|*.avi|" "All files (*.*)|*.*"
            fileDialog = wx.FileDialog(self, message =u"选择单个视频文件", wildcard = filesFilter, style = wx.FD_OPEN)
            dialogResult = fileDialog.ShowModal()
            if dialogResult !=  wx.ID_OK:
                return
            path123 = fileDialog.GetPath()
            self.path1.SetValue(path123)
    def dakaiwenjian1(self,event):
            filesFilter = "视频文件 (*.avi)|*.avi|" "All files (*.*)|*.*"
            fileDialog = wx.FileDialog(self, message ="选择单个视频文件", wildcard = filesFilter, style = wx.FD_OPEN)
            dialogResult = fileDialog.ShowModal()
            if dialogResult !=  wx.ID_OK:
                return
            path123 = fileDialog.GetPath()
            self.path2.SetValue(path123)
    def dakaiwenjian2(self,event):
            filesFilter = "视频文件 (*.avi)|*.avi|" "All files (*.*)|*.*"
            fileDialog = wx.FileDialog(self, message ="选择单个视频文件", wildcard = filesFilter, style = wx.FD_OPEN)
            dialogResult = fileDialog.ShowModal()
            if dialogResult !=  wx.ID_OK:
                return
            path123 = fileDialog.GetPath()
            self.path3.SetValue(path123)

        


if __name__ == '__main__':  
    app = wx.App()
    frame=wx.Frame(None, -1, 'Image', size=(820,530))
    my_panel = MyPanel(frame, -1)  
    frame.Show()  
    app.MainLoop()  



'''
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'相似视频快速甄别检索软件',size=(800,600))
        panel = wx.Panel(self,parent, -1)  
        ##设置背景
        image_file = 'beijing.jpg'  
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()  
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))  
        image_width = to_bmp_image.GetWidth()  
        image_height = to_bmp_image.GetHeight()  
        set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())  
        parent.SetTitle(set_title)  
        #bkg = wx.Image("beijing.jpg",wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #wx.StaticBitmap(panel,-1,bkg,pos=(0,0))
        #panel.Bind(wx.EVT_MOTION, self.OnMove)  
        #wx.StaticText(panel, -1, 'Pos:', pos=(10, 52))  
        #self.posCtrl = wx.TextCtrl(panel, -1, '', pos=(40, 50))
         ##放置主界面按钮
        text1 = wx.StaticText(panel,-1,'请导入原始视频：',pos=(40,70))
        self.path1 = wx.TextCtrl(panel,-1,'',pos=(40,90),size=(250,25))
        self.button1 = wx.Button(panel,-1,'打开',pos=(500,300))
        text2 = wx.StaticText(panel,-1,'请导入待甄别视频：',pos=(40,130))
        self.path2 = wx.TextCtrl(panel,-1,'',pos=(40,150),size=(250,25))

        text3 = wx.StaticText(panel,-1,'请导入原始视频：',pos=(40,70))
        self.path3 = wx.TextCtrl(panel,-1,'',pos=(40,90),size=(250,25))
        #self.button1 = wx.Button(panel,-1,'打开',pos=(500,500))
        text4 = wx.StaticText(panel,-1,'请导入待甄别视频：',pos=(40,130))
        self.path4 = wx.TextCtrl(panel,-1,'',pos=(40,150),size=(250,25))
        
        ##设置菜单
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        self.InitUI()
    def InitUI(self):
 
        menubar = wx.MenuBar()#创建一个菜单栏
        fileMenu = wx.Menu()#创建一个菜单
        newitem = fileMenu.Append(wx.ID_NEW,'新建检索项目')
        fileMenu.AppendSeparator()
        openitem0 = fileMenu.Append(wx.ID_NEW,'打开项目')
        openitem1 = fileMenu.Append(wx.ID_NEW,'快速打开上一次的项目')
        fileMenu.AppendSeparator()
        saveitem0 = fileMenu.Append(wx.ID_NEW,'保存')
        saveitem2 = fileMenu.Append(wx.ID_NEW,'另存为本次项目')
        fileMenu.AppendSeparator()
        fitem = fileMenu.Append(wx.ID_EXIT, '退出', 'Quit application')
        #menubar.Append(fileMenu, '&New')
        menubar.Append(fileMenu, '&文件')

        editMenu = wx.Menu()
        zhengban_item = editMenu.Append(wx.ID_NEW,'导入原版视频')
        editMenu.AppendSeparator()
        jiansuo_item = editMenu.Append(wx.ID_NEW,'导入待检测视频')
        jiansuo_item1 = editMenu.Append(wx.ID_NEW,'批量导入待检测视频')
        menubar.Append(editMenu, '&导入视频文件')

        doMenu = wx.Menu()

        menubar.Append(doMenu, '&检索')
        
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
         
    def OnQuit(self, e):
        self.Close()
          
    def OnMove(self, event):  
        pos = event.GetPosition()  
        self.posCtrl.SetValue('%s, %s' % (pos.x, pos.y))  
          
if __name__ == '__main__':  
    app = wx.App()  
    frame = MyFrame()  
    frame.Show(True)  
    app.MainLoop()
'''
