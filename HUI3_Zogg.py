#Cheryl Zogg HW2

#HUI3 regression coefficients
constant=0.371
factor=1.371
dic_attributes = {'Vision':         [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
                  'Hearing':        [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
                  'Speech':         [1.00, 0.94, 0.89, 0.81, 0.68],
                  'Ambulation':     [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
                  'Dexterity':      [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
                  'Emotion':        [1.00, 0.95, 0.85, 0.64, 0.46],
                  'Cognition':      [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
                  'Pain':           [1.00, 0.96, 0.90, 0.77, 0.55]}

def utility(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """
    :param vision:      ability to see (lower better)
    :param hearing:     ability to hear (lower better)
    :param speech:      ability to talk/be understood (lower better)
    :param ambulation:  ability to walk/move around (lower better)
    :param dexterity:   ability to use hands (lower better)
    :param emotion:     respondant's affect (lower better)
    :param cognition:   ability to remember (lower better)
    :param pain:        level of pain (lower better)
    :return:            health utility level
    """

    #ensuring appropriate dimensionality
    if not(vision in [1,2,3,4,5,6]):
        raise ValueError('Vision level must be 1-6')
    if not(hearing in [1,2,3,4,5,6]):
        raise ValueError('Hearing level must be 1-6')
    if not(speech in [1,2,3,4,5]):
        raise ValueError('Speech level must be 1-5')
    if not(ambulation in [1,2,3,4,5,6]):
        raise ValueError('Ambulation level must be 1-6')
    if not(dexterity in [1,2,3,4,5,6]):
        raise ValueError('Dexterity level must be 1-6')
    if not(emotion in [1,2,3,4,5]):
        raise ValueError('Emotion level must be 1-5')
    if not(cognition in [1,2,3,4,5,6]):
        raise ValueError('Cognition level must be 1-6')
    if not(pain in [1,2,3,4,5]):
        raise ValueError('Pain level must be 1-5')

    level = factor #start by setting level equal to the base multiplier

    #determine coefficients to include in multiplication
    level *= dic_attributes['Vision'][vision-1] #indicated entry shifted 1 to account for frame
    level *= dic_attributes['Hearing'][hearing-1]
    level *= dic_attributes['Speech'][speech-1]
    level *= dic_attributes['Ambulation'][ambulation-1]
    level *= dic_attributes['Dexterity'][dexterity-1]
    level *= dic_attributes['Emotion'][emotion-1]
    level *= dic_attributes['Cognition'][cognition-1]
    level *= dic_attributes['Pain'][pain-1]

    #subtract out the constant
    level -= constant

    return level