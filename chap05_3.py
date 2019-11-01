def updateMaxWidth(numStr, maxWidth):
    currentLength = len(numStr)
    if maxWidth < currentLength:
        maxWidth = currentLength
    return maxWidth


def updateMaxPrecision(numStr, maxPrecision):
    decimalPlaces = numStr[::-1].find('.')
    if (decimalPlaces > maxPrecision):
        maxPrecision = decimalPlaces
    return maxPrecision


def splitFloats(row, maxWidth, maxPrecision):
    isClean = True
    currentRow = []

    for index, numStr in enumerate(row.split()):
        try:
            numFloat = float(numStr)
        except ValueError:
            print("Row includes a non-float string. Do it again.")
            isClean = False
            break

        currentRow.append(numFloat)
        maxWidth = updateMaxWidth(numStr, maxWidth)
        maxPrecision = updateMaxPrecision(numStr, maxPrecision)

        if len(currentRow) == 5:
            break

    return isClean, maxWidth, maxPrecision, currentRow


if '__main__' == __name__:
    rows = []
    maxWidth = maxPrecision = 0

    while len(rows) < 5:
        row = input(f"Enter row of 5 floats: ")
        isClean, maxWidth, maxPrecision, row = splitFloats(
            row, maxWidth, maxPrecision)
        if isClean:
            rows.append(row)

    formattedRows = []
    for row in rows:
        formattedRow = ["{:{}.{}f}".format(
            num, maxWidth, maxPrecision) for num in row]
        formattedRows.append(" ".join(formattedRow))

    print("\n".join(formattedRows))
