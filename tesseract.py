# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tesseract', [dirname(__file__)])
        except ImportError:
            import _tesseract
            return _tesseract
        if fp is not None:
            try:
                _mod = imp.load_module('_tesseract', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _tesseract = swig_import_helper()
    del swig_import_helper
else:
    import _tesseract
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def new_intp():
  return _tesseract.new_intp()
new_intp = _tesseract.new_intp

def copy_intp(*args):
  return _tesseract.copy_intp(*args)
copy_intp = _tesseract.copy_intp

def delete_intp(*args):
  return _tesseract.delete_intp(*args)
delete_intp = _tesseract.delete_intp

def intp_assign(*args):
  return _tesseract.intp_assign(*args)
intp_assign = _tesseract.intp_assign

def intp_value(*args):
  return _tesseract.intp_value(*args)
intp_value = _tesseract.intp_value

def cdata(*args):
  return _tesseract.cdata(*args)
cdata = _tesseract.cdata

def memmove(*args):
  return _tesseract.memmove(*args)
memmove = _tesseract.memmove
PT_UNKNOWN = _tesseract.PT_UNKNOWN
PT_FLOWING_TEXT = _tesseract.PT_FLOWING_TEXT
PT_HEADING_TEXT = _tesseract.PT_HEADING_TEXT
PT_PULLOUT_TEXT = _tesseract.PT_PULLOUT_TEXT
PT_EQUATION = _tesseract.PT_EQUATION
PT_INLINE_EQUATION = _tesseract.PT_INLINE_EQUATION
PT_TABLE = _tesseract.PT_TABLE
PT_VERTICAL_TEXT = _tesseract.PT_VERTICAL_TEXT
PT_CAPTION_TEXT = _tesseract.PT_CAPTION_TEXT
PT_FLOWING_IMAGE = _tesseract.PT_FLOWING_IMAGE
PT_HEADING_IMAGE = _tesseract.PT_HEADING_IMAGE
PT_PULLOUT_IMAGE = _tesseract.PT_PULLOUT_IMAGE
PT_HORZ_LINE = _tesseract.PT_HORZ_LINE
PT_VERT_LINE = _tesseract.PT_VERT_LINE
PT_NOISE = _tesseract.PT_NOISE
PT_COUNT = _tesseract.PT_COUNT

def PTIsLineType(*args):
  return _tesseract.PTIsLineType(*args)
PTIsLineType = _tesseract.PTIsLineType

def PTIsImageType(*args):
  return _tesseract.PTIsImageType(*args)
PTIsImageType = _tesseract.PTIsImageType

def PTIsTextType(*args):
  return _tesseract.PTIsTextType(*args)
PTIsTextType = _tesseract.PTIsTextType
ORIENTATION_PAGE_UP = _tesseract.ORIENTATION_PAGE_UP
ORIENTATION_PAGE_RIGHT = _tesseract.ORIENTATION_PAGE_RIGHT
ORIENTATION_PAGE_DOWN = _tesseract.ORIENTATION_PAGE_DOWN
ORIENTATION_PAGE_LEFT = _tesseract.ORIENTATION_PAGE_LEFT
WRITING_DIRECTION_LEFT_TO_RIGHT = _tesseract.WRITING_DIRECTION_LEFT_TO_RIGHT
WRITING_DIRECTION_RIGHT_TO_LEFT = _tesseract.WRITING_DIRECTION_RIGHT_TO_LEFT
WRITING_DIRECTION_TOP_TO_BOTTOM = _tesseract.WRITING_DIRECTION_TOP_TO_BOTTOM
TEXTLINE_ORDER_LEFT_TO_RIGHT = _tesseract.TEXTLINE_ORDER_LEFT_TO_RIGHT
TEXTLINE_ORDER_RIGHT_TO_LEFT = _tesseract.TEXTLINE_ORDER_RIGHT_TO_LEFT
TEXTLINE_ORDER_TOP_TO_BOTTOM = _tesseract.TEXTLINE_ORDER_TOP_TO_BOTTOM
PSM_OSD_ONLY = _tesseract.PSM_OSD_ONLY
PSM_AUTO_OSD = _tesseract.PSM_AUTO_OSD
PSM_AUTO_ONLY = _tesseract.PSM_AUTO_ONLY
PSM_AUTO = _tesseract.PSM_AUTO
PSM_SINGLE_COLUMN = _tesseract.PSM_SINGLE_COLUMN
PSM_SINGLE_BLOCK_VERT_TEXT = _tesseract.PSM_SINGLE_BLOCK_VERT_TEXT
PSM_SINGLE_BLOCK = _tesseract.PSM_SINGLE_BLOCK
PSM_SINGLE_LINE = _tesseract.PSM_SINGLE_LINE
PSM_SINGLE_WORD = _tesseract.PSM_SINGLE_WORD
PSM_CIRCLE_WORD = _tesseract.PSM_CIRCLE_WORD
PSM_SINGLE_CHAR = _tesseract.PSM_SINGLE_CHAR
PSM_COUNT = _tesseract.PSM_COUNT
RIL_BLOCK = _tesseract.RIL_BLOCK
RIL_PARA = _tesseract.RIL_PARA
RIL_TEXTLINE = _tesseract.RIL_TEXTLINE
RIL_WORD = _tesseract.RIL_WORD
RIL_SYMBOL = _tesseract.RIL_SYMBOL
JUSTIFICATION_UNKNOWN = _tesseract.JUSTIFICATION_UNKNOWN
JUSTIFICATION_LEFT = _tesseract.JUSTIFICATION_LEFT
JUSTIFICATION_CENTER = _tesseract.JUSTIFICATION_CENTER
JUSTIFICATION_RIGHT = _tesseract.JUSTIFICATION_RIGHT
OEM_TESSERACT_ONLY = _tesseract.OEM_TESSERACT_ONLY
OEM_CUBE_ONLY = _tesseract.OEM_CUBE_ONLY
OEM_TESSERACT_CUBE_COMBINED = _tesseract.OEM_TESSERACT_CUBE_COMBINED
OEM_DEFAULT = _tesseract.OEM_DEFAULT
MAX_NUM_INT_FEATURES = _tesseract.MAX_NUM_INT_FEATURES
class TessBaseAPI(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TessBaseAPI, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TessBaseAPI, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _tesseract.new_TessBaseAPI()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tesseract.delete_TessBaseAPI
    __del__ = lambda self : None;
    __swig_getmethods__["Version"] = lambda x: _tesseract.TessBaseAPI_Version
    if _newclass:Version = staticmethod(_tesseract.TessBaseAPI_Version)
    def SetInputName(self, *args): return _tesseract.TessBaseAPI_SetInputName(self, *args)
    def SetOutputName(self, *args): return _tesseract.TessBaseAPI_SetOutputName(self, *args)
    def SetVariable(self, *args): return _tesseract.TessBaseAPI_SetVariable(self, *args)
    def GetIntVariable(self, *args): return _tesseract.TessBaseAPI_GetIntVariable(self, *args)
    def GetBoolVariable(self, *args): return _tesseract.TessBaseAPI_GetBoolVariable(self, *args)
    def GetDoubleVariable(self, *args): return _tesseract.TessBaseAPI_GetDoubleVariable(self, *args)
    def GetStringVariable(self, *args): return _tesseract.TessBaseAPI_GetStringVariable(self, *args)
    def PrintVariables(self, *args): return _tesseract.TessBaseAPI_PrintVariables(self, *args)
    def GetVariableAsString(self, *args): return _tesseract.TessBaseAPI_GetVariableAsString(self, *args)
    def Init(self, *args): return _tesseract.TessBaseAPI_Init(self, *args)
    def InitLangMod(self, *args): return _tesseract.TessBaseAPI_InitLangMod(self, *args)
    def InitForAnalysePage(self): return _tesseract.TessBaseAPI_InitForAnalysePage(self)
    def SetPageSegMode(self, *args): return _tesseract.TessBaseAPI_SetPageSegMode(self, *args)
    def GetPageSegMode(self): return _tesseract.TessBaseAPI_GetPageSegMode(self)
    def TesseractRect(self, *args): return _tesseract.TessBaseAPI_TesseractRect(self, *args)
    def ClearAdaptiveClassifier(self): return _tesseract.TessBaseAPI_ClearAdaptiveClassifier(self)
    def SetImage(self, *args): return _tesseract.TessBaseAPI_SetImage(self, *args)
    def SetRectangle(self, *args): return _tesseract.TessBaseAPI_SetRectangle(self, *args)
    def GetThresholdedImage(self): return _tesseract.TessBaseAPI_GetThresholdedImage(self)
    def GetRegions(self, *args): return _tesseract.TessBaseAPI_GetRegions(self, *args)
    def GetTextlines(self, *args): return _tesseract.TessBaseAPI_GetTextlines(self, *args)
    def GetWords(self, *args): return _tesseract.TessBaseAPI_GetWords(self, *args)
    def GetConnectedComponents(self, *args): return _tesseract.TessBaseAPI_GetConnectedComponents(self, *args)
    def DumpPGM(self, *args): return _tesseract.TessBaseAPI_DumpPGM(self, *args)
    def AnalyseLayout(self): return _tesseract.TessBaseAPI_AnalyseLayout(self)
    def Recognize(self, *args): return _tesseract.TessBaseAPI_Recognize(self, *args)
    def RecognizeForChopTest(self, *args): return _tesseract.TessBaseAPI_RecognizeForChopTest(self, *args)
    def ProcessPages(self, *args): return _tesseract.TessBaseAPI_ProcessPages(self, *args)
    def ProcessPage(self, *args): return _tesseract.TessBaseAPI_ProcessPage(self, *args)
    def GetIterator(self): return _tesseract.TessBaseAPI_GetIterator(self)
    def GetUTF8Text(self): return _tesseract.TessBaseAPI_GetUTF8Text(self)
    def GetHOCRText(self, *args): return _tesseract.TessBaseAPI_GetHOCRText(self, *args)
    def GetBoxText(self, *args): return _tesseract.TessBaseAPI_GetBoxText(self, *args)
    def GetUNLVText(self): return _tesseract.TessBaseAPI_GetUNLVText(self)
    def MeanTextConf(self): return _tesseract.TessBaseAPI_MeanTextConf(self)
    def AllWordConfidences(self): return _tesseract.TessBaseAPI_AllWordConfidences(self)
    def AdaptToWordStr(self, *args): return _tesseract.TessBaseAPI_AdaptToWordStr(self, *args)
    def Clear(self): return _tesseract.TessBaseAPI_Clear(self)
    def End(self): return _tesseract.TessBaseAPI_End(self)
    def IsValidWord(self, *args): return _tesseract.TessBaseAPI_IsValidWord(self, *args)
    def GetTextDirection(self, *args): return _tesseract.TessBaseAPI_GetTextDirection(self, *args)
    def DetectOS(self, *args): return _tesseract.TessBaseAPI_DetectOS(self, *args)
    def GetFeaturesForBlob(self, *args): return _tesseract.TessBaseAPI_GetFeaturesForBlob(self, *args)
    __swig_getmethods__["FindRowForBox"] = lambda x: _tesseract.TessBaseAPI_FindRowForBox
    if _newclass:FindRowForBox = staticmethod(_tesseract.TessBaseAPI_FindRowForBox)
    def RunAdaptiveClassifier(self, *args): return _tesseract.TessBaseAPI_RunAdaptiveClassifier(self, *args)
    def GetUnichar(self, *args): return _tesseract.TessBaseAPI_GetUnichar(self, *args)
    def GetDawg(self, *args): return _tesseract.TessBaseAPI_GetDawg(self, *args)
    def NumDawgs(self): return _tesseract.TessBaseAPI_NumDawgs(self)
    __swig_getmethods__["MakeTessOCRRow"] = lambda x: _tesseract.TessBaseAPI_MakeTessOCRRow
    if _newclass:MakeTessOCRRow = staticmethod(_tesseract.TessBaseAPI_MakeTessOCRRow)
    __swig_getmethods__["MakeTBLOB"] = lambda x: _tesseract.TessBaseAPI_MakeTBLOB
    if _newclass:MakeTBLOB = staticmethod(_tesseract.TessBaseAPI_MakeTBLOB)
    __swig_getmethods__["NormalizeTBLOB"] = lambda x: _tesseract.TessBaseAPI_NormalizeTBLOB
    if _newclass:NormalizeTBLOB = staticmethod(_tesseract.TessBaseAPI_NormalizeTBLOB)
    def tesseract(self): return _tesseract.TessBaseAPI_tesseract(self)
    def oem(self): return _tesseract.TessBaseAPI_oem(self)
    def InitTruthCallback(self, *args): return _tesseract.TessBaseAPI_InitTruthCallback(self, *args)
    def GetCubeRecoContext(self): return _tesseract.TessBaseAPI_GetCubeRecoContext(self)
    def set_min_orientation_margin(self, *args): return _tesseract.TessBaseAPI_set_min_orientation_margin(self, *args)
    def GetBlockTextOrientations(self, *args): return _tesseract.TessBaseAPI_GetBlockTextOrientations(self, *args)
    def FindLinesCreateBlockList(self): return _tesseract.TessBaseAPI_FindLinesCreateBlockList(self)
    __swig_getmethods__["DeleteBlockList"] = lambda x: _tesseract.TessBaseAPI_DeleteBlockList
    if _newclass:DeleteBlockList = staticmethod(_tesseract.TessBaseAPI_DeleteBlockList)
TessBaseAPI_swigregister = _tesseract.TessBaseAPI_swigregister
TessBaseAPI_swigregister(TessBaseAPI)
cvar = _tesseract.cvar
kPointsPerInch = cvar.kPointsPerInch

def TessBaseAPI_Version():
  return _tesseract.TessBaseAPI_Version()
TessBaseAPI_Version = _tesseract.TessBaseAPI_Version

def TessBaseAPI_FindRowForBox(*args):
  return _tesseract.TessBaseAPI_FindRowForBox(*args)
TessBaseAPI_FindRowForBox = _tesseract.TessBaseAPI_FindRowForBox

def TessBaseAPI_MakeTessOCRRow(*args):
  return _tesseract.TessBaseAPI_MakeTessOCRRow(*args)
TessBaseAPI_MakeTessOCRRow = _tesseract.TessBaseAPI_MakeTessOCRRow

def TessBaseAPI_MakeTBLOB(*args):
  return _tesseract.TessBaseAPI_MakeTBLOB(*args)
TessBaseAPI_MakeTBLOB = _tesseract.TessBaseAPI_MakeTBLOB

def TessBaseAPI_NormalizeTBLOB(*args):
  return _tesseract.TessBaseAPI_NormalizeTBLOB(*args)
TessBaseAPI_NormalizeTBLOB = _tesseract.TessBaseAPI_NormalizeTBLOB

def TessBaseAPI_DeleteBlockList(*args):
  return _tesseract.TessBaseAPI_DeleteBlockList(*args)
TessBaseAPI_DeleteBlockList = _tesseract.TessBaseAPI_DeleteBlockList


def is_iplimage(*args):
  return _tesseract.is_iplimage(*args)
is_iplimage = _tesseract.is_iplimage

def is_cvmat(*args):
  return _tesseract.is_cvmat(*args)
is_cvmat = _tesseract.is_cvmat

def is_cvmatnd(*args):
  return _tesseract.is_cvmatnd(*args)
is_cvmatnd = _tesseract.is_cvmatnd

def convert_to_CvArr(*args):
  return _tesseract.convert_to_CvArr(*args)
convert_to_CvArr = _tesseract.convert_to_CvArr

def convert_to_IplImage(*args):
  return _tesseract.convert_to_IplImage(*args)
convert_to_IplImage = _tesseract.convert_to_IplImage

def convert_to_CvMat(*args):
  return _tesseract.convert_to_CvMat(*args)
convert_to_CvMat = _tesseract.convert_to_CvMat

def convert_to_CvMatND(*args):
  return _tesseract.convert_to_CvMatND(*args)
convert_to_CvMatND = _tesseract.convert_to_CvMatND

def what_data(*args):
  return _tesseract.what_data(*args)
what_data = _tesseract.what_data

def isLibTiff():
  return _tesseract.isLibTiff()
isLibTiff = _tesseract.isLibTiff

def isLibLept():
  return _tesseract.isLibLept()
isLibLept = _tesseract.isLibLept

def ProcessPagesWrapper(*args):
  return _tesseract.ProcessPagesWrapper(*args)
ProcessPagesWrapper = _tesseract.ProcessPagesWrapper

def ProcessPagesPix(*args):
  return _tesseract.ProcessPagesPix(*args)
ProcessPagesPix = _tesseract.ProcessPagesPix

def ProcessPagesFileStream(*args):
  return _tesseract.ProcessPagesFileStream(*args)
ProcessPagesFileStream = _tesseract.ProcessPagesFileStream

def ProcessPagesBuffer(*args):
  return _tesseract.ProcessPagesBuffer(*args)
ProcessPagesBuffer = _tesseract.ProcessPagesBuffer

def ProcessPagesRaw(*args):
  return _tesseract.ProcessPagesRaw(*args)
ProcessPagesRaw = _tesseract.ProcessPagesRaw

def SetCvImage(*args):
  return _tesseract.SetCvImage(*args)
SetCvImage = _tesseract.SetCvImage

def SetVariable(*args):
  return _tesseract.SetVariable(*args)
SetVariable = _tesseract.SetVariable

def GetUTF8Text(*args):
  return _tesseract.GetUTF8Text(*args)
GetUTF8Text = _tesseract.GetUTF8Text
# This file is compatible with both classic and new-style classes.


