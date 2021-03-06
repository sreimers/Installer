from reaper_python import *

def BR_EnvAlloc(p0,p1):
  a=rpr_getfp('BR_EnvAlloc')
  f=CFUNCTYPE(c_uint64,c_uint64,c_byte)(a)
  t=(rpr_packp('TrackEnvelope*',p0),c_byte(p1))
  r=f(t[0],t[1])
  return rpr_unpackp('BR_Envelope*',r)

def BR_EnvCountPoints(p0):
  a=rpr_getfp('BR_EnvCountPoints')
  f=CFUNCTYPE(c_int,c_uint64)(a)
  t=(rpr_packp('BR_Envelope*',p0),)
  r=f(t[0])
  return r

def BR_EnvDeletePoint(p0,p1):
  a=rpr_getfp('BR_EnvDeletePoint')
  f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_int(p1))
  r=f(t[0],t[1])
  return r

def BR_EnvFind(p0,p1,p2):
  a=rpr_getfp('BR_EnvFind')
  f=CFUNCTYPE(c_int,c_uint64,c_double,c_double)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_double(p1),c_double(p2))
  r=f(t[0],t[1],t[2])
  return r

def BR_EnvFindNext(p0,p1):
  a=rpr_getfp('BR_EnvFindNext')
  f=CFUNCTYPE(c_int,c_uint64,c_double)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_double(p1))
  r=f(t[0],t[1])
  return r

def BR_EnvFindPrevious(p0,p1):
  a=rpr_getfp('BR_EnvFindPrevious')
  f=CFUNCTYPE(c_int,c_uint64,c_double)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_double(p1))
  r=f(t[0],t[1])
  return r

def BR_EnvFree(p0,p1):
  a=rpr_getfp('BR_EnvFree')
  f=CFUNCTYPE(c_byte,c_uint64,c_byte)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_byte(p1))
  r=f(t[0],t[1])
  return r

def BR_EnvGetParentTake(p0):
  a=rpr_getfp('BR_EnvGetParentTake')
  f=CFUNCTYPE(c_uint64,c_uint64)(a)
  t=(rpr_packp('BR_Envelope*',p0),)
  r=f(t[0])
  return rpr_unpackp('MediaItem_Take*',r)

def BR_EnvGetParentTrack(p0):
  a=rpr_getfp('BR_EnvGetParentTrack')
  f=CFUNCTYPE(c_uint64,c_uint64)(a)
  t=(rpr_packp('BR_Envelope*',p0),)
  r=f(t[0])
  return rpr_unpackp('MediaItem*',r)

def BR_EnvGetPoint(p0,p1,p2,p3,p4,p5,p6):
  a=rpr_getfp('BR_EnvGetPoint')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_int(p1),c_double(p2),c_double(p3),c_int(p4),c_byte(p5),c_double(p6))
  r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
  return (r,p0,p1,float(t[2].value),float(t[3].value),int(t[4].value),int(t[5].value),float(t[6].value))

def BR_EnvGetProperties(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
  a=rpr_getfp('BR_EnvGetProperties')
  f=CFUNCTYPE(None,c_uint64,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_byte(p1),c_byte(p2),c_byte(p3),c_byte(p4),c_int(p5),c_int(p6),c_double(p7),c_double(p8),c_double(p9),c_int(p10))
  f(t[0],byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]),byref(t[9]),byref(t[10]))
  return (p0,int(t[1].value),int(t[2].value),int(t[3].value),int(t[4].value),int(t[5].value),int(t[6].value),float(t[7].value),float(t[8].value),float(t[9].value),int(t[10].value))

def BR_EnvSetPoint(p0,p1,p2,p3,p4,p5,p6):
  a=rpr_getfp('BR_EnvSetPoint')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_double,c_int,c_byte,c_double)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_int(p1),c_double(p2),c_double(p3),c_int(p4),c_byte(p5),c_double(p6))
  r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
  return r

def BR_EnvSetProperties(p0,p1,p2,p3,p4,p5,p6):
  a=rpr_getfp('BR_EnvSetProperties')
  f=CFUNCTYPE(None,c_uint64,c_byte,c_byte,c_byte,c_byte,c_int,c_int)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_byte(p1),c_byte(p2),c_byte(p3),c_byte(p4),c_int(p5),c_int(p6))
  f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])

def BR_EnvValueAtPos(p0,p1):
  a=rpr_getfp('BR_EnvValueAtPos')
  f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
  t=(rpr_packp('BR_Envelope*',p0),c_double(p1))
  r=f(t[0],t[1])
  return r

def BR_GetMediaSourceProperties(p0,p1,p2,p3,p4,p5):
  a=rpr_getfp('BR_GetMediaSourceProperties')
  f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
  t=(rpr_packp('MediaItem_Take*',p0),c_byte(p1),c_double(p2),c_double(p3),c_double(p4),c_byte(p5))
  r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]))
  return (r,p0,int(t[1].value),float(t[2].value),float(t[3].value),float(t[4].value),int(t[5].value))

def BR_GetMouseCursorContext(p0,p1,p2,p3):
  a=rpr_getfp('BR_GetMouseCursorContext')
  f=CFUNCTYPE(None,c_char_p,c_char_p,c_char_p,c_int)(a)
  t=(rpr_packs(p0),rpr_packs(p1),rpr_packs(p2),c_int(p3))
  f(t[0],t[1],t[2],t[3])
  return (rpr_unpacks(t[0]),rpr_unpacks(t[1]),rpr_unpacks(t[2]),p3)

def BR_GetMouseCursorContext_Envelope(p0):
  a=rpr_getfp('BR_GetMouseCursorContext_Envelope')
  f=CFUNCTYPE(c_uint64,c_void_p)(a)
  t=(c_byte(p0),)
  r=f(byref(t[0]))
  return (rpr_unpackp('TrackEnvelope*',r),int(t[0].value))

def BR_GetMouseCursorContext_Item():
  a=rpr_getfp('BR_GetMouseCursorContext_Item')
  f=CFUNCTYPE(c_uint64)(a)
  r=f()
  return rpr_unpackp('MediaItem*',r)

def BR_GetMouseCursorContext_MIDI(p0,p1,p2,p3,p4):
  a=rpr_getfp('BR_GetMouseCursorContext_MIDI')
  f=CFUNCTYPE(c_uint64,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
  t=(c_byte(p0),c_int(p1),c_int(p2),c_int(p3),c_int(p4))
  r=f(byref(t[0]),byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]))
  return (rpr_unpackp('void*',r),int(t[0].value),int(t[1].value),int(t[2].value),int(t[3].value),int(t[4].value))

def BR_GetMouseCursorContext_Position():
  a=rpr_getfp('BR_GetMouseCursorContext_Position')
  f=CFUNCTYPE(c_double)(a)
  r=f()
  return r

def BR_GetMouseCursorContext_StretchMarker():
  a=rpr_getfp('BR_GetMouseCursorContext_StretchMarker')
  f=CFUNCTYPE(c_int)(a)
  r=f()
  return r

def BR_GetMouseCursorContext_Take():
  a=rpr_getfp('BR_GetMouseCursorContext_Take')
  f=CFUNCTYPE(c_uint64)(a)
  r=f()
  return rpr_unpackp('MediaItem_Take*',r)

def BR_GetMouseCursorContext_Track():
  a=rpr_getfp('BR_GetMouseCursorContext_Track')
  f=CFUNCTYPE(c_uint64)(a)
  r=f()
  return rpr_unpackp('MediaTrack*',r)

def BR_ItemAtMouseCursor(p0):
  a=rpr_getfp('BR_ItemAtMouseCursor')
  f=CFUNCTYPE(c_uint64,c_void_p)(a)
  t=(c_double(p0),)
  r=f(byref(t[0]))
  return (rpr_unpackp('MediaItem*',r),float(t[0].value))

def BR_MIDI_CCLaneRemove(p0,p1):
  a=rpr_getfp('BR_MIDI_CCLaneRemove')
  f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
  t=(rpr_packp('void*',p0),c_int(p1))
  r=f(t[0],t[1])
  return r

def BR_MIDI_CCLaneReplace(p0,p1,p2):
  a=rpr_getfp('BR_MIDI_CCLaneReplace')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
  t=(rpr_packp('void*',p0),c_int(p1),c_int(p2))
  r=f(t[0],t[1],t[2])
  return r

def BR_PositionAtMouseCursor(p0):
  a=rpr_getfp('BR_PositionAtMouseCursor')
  f=CFUNCTYPE(c_double,c_byte)(a)
  t=(c_byte(p0),)
  r=f(t[0])
  return r

def BR_SetMediaSourceProperties(p0,p1,p2,p3,p4,p5):
  a=rpr_getfp('BR_SetMediaSourceProperties')
  f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_double,c_double,c_double,c_byte)(a)
  t=(rpr_packp('MediaItem_Take*',p0),c_byte(p1),c_double(p2),c_double(p3),c_double(p4),c_byte(p5))
  r=f(t[0],t[1],t[2],t[3],t[4],t[5])
  return r

def BR_SetTakeSourceFromFile(p0,p1,p2):
  a=rpr_getfp('BR_SetTakeSourceFromFile')
  f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte)(a)
  t=(rpr_packp('MediaItem_Take*',p0),rpr_packsc(p1),c_byte(p2))
  r=f(t[0],t[1],t[2])
  return r

def BR_SetTakeSourceFromFile2(p0,p1,p2,p3):
  a=rpr_getfp('BR_SetTakeSourceFromFile2')
  f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte,c_byte)(a)
  t=(rpr_packp('MediaItem_Take*',p0),rpr_packsc(p1),c_byte(p2),c_byte(p3))
  r=f(t[0],t[1],t[2],t[3])
  return r

def BR_TakeAtMouseCursor(p0):
  a=rpr_getfp('BR_TakeAtMouseCursor')
  f=CFUNCTYPE(c_uint64,c_void_p)(a)
  t=(c_double(p0),)
  r=f(byref(t[0]))
  return (rpr_unpackp('MediaItem_Take*',r),float(t[0].value))

def BR_TrackAtMouseCursor(p0,p1):
  a=rpr_getfp('BR_TrackAtMouseCursor')
  f=CFUNCTYPE(c_uint64,c_void_p,c_void_p)(a)
  t=(c_int(p0),c_double(p1))
  r=f(byref(t[0]),byref(t[1]))
  return (rpr_unpackp('MediaTrack*',r),int(t[0].value),float(t[1].value))

def FNG_AddMidiNote(p0):
  a=rpr_getfp('FNG_AddMidiNote')
  f=CFUNCTYPE(c_uint64,c_uint64)(a)
  t=(rpr_packp('RprMidiTake*',p0),)
  r=f(t[0])
  return rpr_unpackp('RprMidiNote*',r)

def FNG_AllocMidiTake(p0):
  a=rpr_getfp('FNG_AllocMidiTake')
  f=CFUNCTYPE(c_uint64,c_uint64)(a)
  t=(rpr_packp('MediaItem_Take*',p0),)
  r=f(t[0])
  return rpr_unpackp('RprMidiTake*',r)

def FNG_CountMidiNotes(p0):
  a=rpr_getfp('FNG_CountMidiNotes')
  f=CFUNCTYPE(c_int,c_uint64)(a)
  t=(rpr_packp('RprMidiTake*',p0),)
  r=f(t[0])
  return r

def FNG_FreeMidiTake(p0):
  a=rpr_getfp('FNG_FreeMidiTake')
  f=CFUNCTYPE(None,c_uint64)(a)
  t=(rpr_packp('RprMidiTake*',p0),)
  f(t[0])

def FNG_GetMidiNote(p0,p1):
  a=rpr_getfp('FNG_GetMidiNote')
  f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
  t=(rpr_packp('RprMidiTake*',p0),c_int(p1))
  r=f(t[0],t[1])
  return rpr_unpackp('RprMidiNote*',r)

def FNG_GetMidiNoteIntProperty(p0,p1):
  a=rpr_getfp('FNG_GetMidiNoteIntProperty')
  f=CFUNCTYPE(c_int,c_uint64,c_char_p)(a)
  t=(rpr_packp('RprMidiNote*',p0),rpr_packsc(p1))
  r=f(t[0],t[1])
  return r

def FNG_SetMidiNoteIntProperty(p0,p1,p2):
  a=rpr_getfp('FNG_SetMidiNoteIntProperty')
  f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
  t=(rpr_packp('RprMidiNote*',p0),rpr_packsc(p1),c_int(p2))
  f(t[0],t[1],t[2])

def SNM_AddReceive(p0,p1,p2):
  a=rpr_getfp('SNM_AddReceive')
  f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_int)(a)
  t=(rpr_packp('MediaTrack*',p0),rpr_packp('MediaTrack*',p1),c_int(p2))
  r=f(t[0],t[1],t[2])
  return r

def SNM_AddTCPFXParm(p0,p1,p2):
  a=rpr_getfp('SNM_AddTCPFXParm')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
  t=(rpr_packp('MediaTrack*',p0),c_int(p1),c_int(p2))
  r=f(t[0],t[1],t[2])
  return r

def SNM_CreateFastString(p0):
  a=rpr_getfp('SNM_CreateFastString')
  f=CFUNCTYPE(c_uint64,c_char_p)(a)
  t=(rpr_packsc(p0),)
  r=f(t[0])
  return rpr_unpackp('WDL_FastString*',r)

def SNM_DeleteFastString(p0):
  a=rpr_getfp('SNM_DeleteFastString')
  f=CFUNCTYPE(None,c_uint64)(a)
  t=(rpr_packp('WDL_FastString*',p0),)
  f(t[0])

def SNM_GetDoubleConfigVar(p0,p1):
  a=rpr_getfp('SNM_GetDoubleConfigVar')
  f=CFUNCTYPE(c_double,c_char_p,c_double)(a)
  t=(rpr_packsc(p0),c_double(p1))
  r=f(t[0],t[1])
  return r

def SNM_GetFastString(p0):
  a=rpr_getfp('SNM_GetFastString')
  f=CFUNCTYPE(c_char_p,c_uint64)(a)
  t=(rpr_packp('WDL_FastString*',p0),)
  r=f(t[0])
  return str(r.decode())

def SNM_GetFastStringLength(p0):
  a=rpr_getfp('SNM_GetFastStringLength')
  f=CFUNCTYPE(c_int,c_uint64)(a)
  t=(rpr_packp('WDL_FastString*',p0),)
  r=f(t[0])
  return r

def SNM_GetIntConfigVar(p0,p1):
  a=rpr_getfp('SNM_GetIntConfigVar')
  f=CFUNCTYPE(c_int,c_char_p,c_int)(a)
  t=(rpr_packsc(p0),c_int(p1))
  r=f(t[0],t[1])
  return r

def SNM_GetMediaItemTakeByGUID(p0,p1):
  a=rpr_getfp('SNM_GetMediaItemTakeByGUID')
  f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
  t=(rpr_packp('ReaProject*',p0),rpr_packsc(p1))
  r=f(t[0],t[1])
  return rpr_unpackp('MediaItem_Take*',r)

def SNM_GetMIDIEditorActiveTake():
  a=rpr_getfp('SNM_GetMIDIEditorActiveTake')
  f=CFUNCTYPE(c_uint64)(a)
  r=f()
  return rpr_unpackp('MediaItem_Take*',r)

def SNM_GetProjectMarkerName(p0,p1,p2,p3):
  a=rpr_getfp('SNM_GetProjectMarkerName')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_uint64)(a)
  t=(rpr_packp('ReaProject*',p0),c_int(p1),c_byte(p2),rpr_packp('WDL_FastString*',p3))
  r=f(t[0],t[1],t[2],t[3])
  return r

def SNM_GetSetObjectState(p0,p1,p2,p3):
  a=rpr_getfp('SNM_GetSetObjectState')
  f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_byte,c_byte)(a)
  t=(rpr_packp('void*',p0),rpr_packp('WDL_FastString*',p1),c_byte(p2),c_byte(p3))
  r=f(t[0],t[1],t[2],t[3])
  return r

def SNM_GetSetSourceState(p0,p1,p2,p3):
  a=rpr_getfp('SNM_GetSetSourceState')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_uint64,c_byte)(a)
  t=(rpr_packp('MediaItem*',p0),c_int(p1),rpr_packp('WDL_FastString*',p2),c_byte(p3))
  r=f(t[0],t[1],t[2],t[3])
  return r

def SNM_GetSetSourceState2(p0,p1,p2):
  a=rpr_getfp('SNM_GetSetSourceState2')
  f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_byte)(a)
  t=(rpr_packp('MediaItem_Take*',p0),rpr_packp('WDL_FastString*',p1),c_byte(p2))
  r=f(t[0],t[1],t[2])
  return r

def SNM_GetSourceType(p0,p1):
  a=rpr_getfp('SNM_GetSourceType')
  f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
  t=(rpr_packp('MediaItem_Take*',p0),rpr_packp('WDL_FastString*',p1))
  r=f(t[0],t[1])
  return r

def SNM_MoveOrRemoveTrackFX(p0,p1,p2):
  a=rpr_getfp('SNM_MoveOrRemoveTrackFX')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
  t=(rpr_packp('MediaTrack*',p0),c_int(p1),c_int(p2))
  r=f(t[0],t[1],t[2])
  return r

def SNM_RemoveReceive(p0,p1):
  a=rpr_getfp('SNM_RemoveReceive')
  f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
  t=(rpr_packp('MediaTrack*',p0),c_int(p1))
  r=f(t[0],t[1])
  return r

def SNM_RemoveReceivesFrom(p0,p1):
  a=rpr_getfp('SNM_RemoveReceivesFrom')
  f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
  t=(rpr_packp('MediaTrack*',p0),rpr_packp('MediaTrack*',p1))
  r=f(t[0],t[1])
  return r

def SNM_SelectResourceBookmark(p0):
  a=rpr_getfp('SNM_SelectResourceBookmark')
  f=CFUNCTYPE(c_int,c_char_p)(a)
  t=(rpr_packsc(p0),)
  r=f(t[0])
  return r

def SNM_SetDoubleConfigVar(p0,p1):
  a=rpr_getfp('SNM_SetDoubleConfigVar')
  f=CFUNCTYPE(c_byte,c_char_p,c_double)(a)
  t=(rpr_packsc(p0),c_double(p1))
  r=f(t[0],t[1])
  return r

def SNM_SetFastString(p0,p1):
  a=rpr_getfp('SNM_SetFastString')
  f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
  t=(rpr_packp('WDL_FastString*',p0),rpr_packsc(p1))
  r=f(t[0],t[1])
  return rpr_unpackp('WDL_FastString*',r)

def SNM_SetIntConfigVar(p0,p1):
  a=rpr_getfp('SNM_SetIntConfigVar')
  f=CFUNCTYPE(c_byte,c_char_p,c_int)(a)
  t=(rpr_packsc(p0),c_int(p1))
  r=f(t[0],t[1])
  return r

def SNM_SetProjectMarker(p0,p1,p2,p3,p4,p5,p6):
  a=rpr_getfp('SNM_SetProjectMarker')
  f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_char_p,c_int)(a)
  t=(rpr_packp('ReaProject*',p0),c_int(p1),c_byte(p2),c_double(p3),c_double(p4),rpr_packsc(p5),c_int(p6))
  r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
  return r

def SNM_TieResourceSlotActions(p0):
  a=rpr_getfp('SNM_TieResourceSlotActions')
  f=CFUNCTYPE(None,c_int)(a)
  t=(c_int(p0),)
  f(t[0])

def ULT_GetMediaItemNote(p0):
  a=rpr_getfp('ULT_GetMediaItemNote')
  f=CFUNCTYPE(c_char_p,c_uint64)(a)
  t=(rpr_packp('MediaItem*',p0),)
  r=f(t[0])
  return str(r.decode())

def ULT_SetMediaItemNote(p0,p1):
  a=rpr_getfp('ULT_SetMediaItemNote')
  f=CFUNCTYPE(None,c_uint64,c_char_p)(a)
  t=(rpr_packp('MediaItem*',p0),rpr_packs(p1))
  f(t[0],t[1])
  return (p0,rpr_unpacks(t[1]))

