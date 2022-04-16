MoveIncrements = 30

ScrollHor = 1

;change increments
NumpadEnter::
if not (GetKeyState("NumLock", "T"))
    return

InputBox, UserInput, Move Increments, Please enter move increments (30), , 235, 120
if ErrorLevel
    return
else
    if UserInput is Not Integer
    {
        MsgBox, You entered "%UserInput%", which is invalid, move set to 30
        MoveIncrements := 30
        return
    }
    MoveIncrements := UserInput
return

;change scroll
NumpadDot::
ScrollHor := !ScrollHor
return

;scroll up
Numpad2::
if (ScrollHor == True){
    Send {WheelLeft}
    return
}
Send {WheelUp}
return

;scroll down
Numpad3::
if (ScrollHor == True){
    Send {WheelRight}
    return
}
Send {WheelDown}
return

;right down
Numpad0::
Click Down RIGHT
Return

;left down
Numpad1::
Click Down LEFT
Return

;left click
Numpad7::
MouseClick, LEFT, , , 1
Return

;right click
Numpad9::
MouseClick, Right, , , 1
Return

mouseXY(x,y)
{
;DllCall("SetCursorPos", "int", X, "int", Y)
DllCall("mouse_event",uint,1,int,x,int,y,uint,0,int,0)
}

;up
Numpad8::
CoordMode, Mouse, Screen
MouseGetPos, X, Y
Y += -MoveIncrements
mouseXY(0, -MoveIncrements)
Return

;down
Numpad5::
CoordMode, Mouse, Screen
MouseGetPos, X, Y
Y += MoveIncrements
mouseXY(0, MoveIncrements)
Return

;left
Numpad4::
CoordMode, Mouse, Screen
MouseGetPos, X, Y
X += -MoveIncrements
mouseXY(-MoveIncrements, 0)
Return

;right
Numpad6::
CoordMode, Mouse, Screen
MouseGetPos, X, Y
X += MoveIncrements
mouseXY(MoveIncrements, 0)
Return
