// When event 'submit' occurs on sizePicker form, call formSubmit()
let sizePicker = document.getElementById('sizePicker');
sizePicker.addEventListener('submit', function (event) {
    formSubmit();
});

// Collects grid size from sizePicker form and passes to makeGrid() call
function formSubmit() {
    event.preventDefault();
    let inputHeight = document.getElementById('inputHeight').value;
    let inputWidth = document.getElementById('inputWidth').value;
    makeGrid(inputHeight, inputWidth);
}

// Creates pixelCanvas grid from sizePicker values, passed from formSubmit()
function makeGrid(inputHeight, inputWidth) {

    // Get table information and create empty grid to populate from sizePicker
    let canvas = document.getElementById('pixelCanvas');
    let canvasGrid = '';

    // Loop det. grid height, build HTML string to replace table below w/ canvasGrid
    for (let i = 0; i < inputHeight; i++) {
        canvasGrid += '<tr class="row-' + i + '">';
        // Loop det. grid width, build HTML string to replace table below w/ canvasGrid
        for (let j = 0; j < inputWidth; j++) {
            canvasGrid += '<td class="cell" id="row-' + i + '_cell-' + j + '"></td>';
        }
        canvasGrid += '</tr>';
    }

    // Replace current table element with new grid string created from above loops
    canvas.innerHTML = canvasGrid;

    // Apply event listeners to cell grid
    onCellClick();
}

// Add click event listener to grid cells, applying current color
function onCellClick() {
    let colorPicker = document.getElementById('colorPicker');
    let gridCells = document.getElementsByClassName('cell');
    
    // Loop over current grid, applying click event listener to each cell.
    for (let i = 0; i < gridCells.length; i++) {
        gridCells[i].addEventListener('click', function (event) {
            // Event to change cell color based on current color selection from colorPicker
            let clickedCell = event.target;
            clickedCell.style.backgroundColor = colorPicker.value;
        });
    }
}