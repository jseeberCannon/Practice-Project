label outside:

    d "So [povname] who do you think we should ask first?"

    show detective at right with moveinright

    show suspect1 at left with dissolve

    s "Well hey there you two! Could you two please take a moment to listen to my woes?"

    d "..."

    p "..."

    p "Sorry but we are trying to solve the recent murder case"

    s "Oh that little thing? Some were saying it was an accident, Other's say it was done on purpose"

    s "Well either way I suppose you need my testimony don't you?"

    d "That's correct"

    menu:
        "Ask For Testimony":
            jump testimony

        "Go to the Crime Scene":
            jump inside
