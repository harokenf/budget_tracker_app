// Temporary data
let categories = [
    { id: 1, name: 'Lebensmittel', color: '#EF4444', limit: 500 },
    { id: 2, name: 'Transport', color: '#3B82F6', limit: 300 },
    { id: 3, name: 'Unterhaltung', color: '#10B981', limit: 200 }
];

// Select a predefined color
function selectColor(color) {
    document.getElementById('newCategoryColor').value = color;
    document.getElementById('colorHex').value = color.toUpperCase();
}

// Synchronize the color picker with the hex field
document.addEventListener('DOMContentLoaded', function() {
    const colorInput = document.getElementById('newCategoryColor');
    const colorHex = document.getElementById('colorHex');
    
    if (colorInput && colorHex) {
        colorInput.addEventListener('input', function(e) {
            colorHex.value = e.target.value.toUpperCase();
        });
    }
});

// Reset the form
function resetCategoryForm() {
    document.getElementById('newCategoryName').value = '';
    document.getElementById('newCategoryColor').value = '#3B82F6';
    document.getElementById('colorHex').value = '#3B82F6';
    document.getElementById('newCategoryLimit').value = '';
}

// Save a new category
function saveNewCategory() {
    const name = document.getElementById('newCategoryName').value.trim();
    const color = document.getElementById('newCategoryColor').value;
    const limit = parseFloat(document.getElementById('newCategoryLimit').value);

    // Validation
    if (!name) {
        alert('Bitte geben Sie einen Namen ein!');
        document.getElementById('newCategoryName').focus();
        return;
    }
    if (!limit || limit <= 0) {
        alert('Bitte geben Sie ein gültiges Limit ein!');
        document.getElementById('newCategoryLimit').focus();
        return;
    }

    // Add category
    const newId = categories.length > 0 ? Math.max(...categories.map(c => c.id)) + 1 : 1;
    categories.push({ 
        id: newId, 
        name: name, 
        color: color, 
        limit: limit
    });

    // Refresh the display
    renderCategories();
    
    // Reset the form
    resetCategoryForm();
    
    // Notification
    showNotification(`Kategorie "${name}" erfolgreich hinzugefügt!`, 'success');

    // TODO: Send to the backend
    console.log('Neue Kategorie:', { name, color, limit });
}

// Edit a category
function editCategory(id) {
    const category = categories.find(c => c.id === id);
    if (!category) return;

    const newName = prompt('Neuer Name:', category.name);
    if (newName && newName.trim()) {
        category.name = newName.trim();
        renderCategories();
        showNotification('Kategorie aktualisiert!', 'success');
        
        // TODO: Send to the backend
        console.log('Catégorie modifiée:', category);
    }
}

// Delete a category
function deleteCategory(id) {
    const category = categories.find(c => c.id === id);
    if (!category) return;

    if (confirm(`Möchten Sie die Kategorie "${category.name}" wirklich löschen?`)) {
        categories = categories.filter(c => c.id !== id);
        renderCategories();
        showNotification('Kategorie gelöscht!', 'success');
        
        // TODO: Send to the backend
        console.log('Catégorie supprimée:', id);
    }
}

// Show categories
function renderCategories() {
    const container = document.getElementById('categories-list');
    if (!container) return;
    
    container.innerHTML = '';
    
    categories.forEach(category => {
        const div = document.createElement('div');
        div.className = 'flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition';
        div.innerHTML = `
            <div class="flex items-center space-x-4">
                <div class="w-6 h-6 rounded-lg" style="background-color: ${category.color};"></div>
                <div>
                    <p class="font-medium">${category.name}</p>
                    <p class="text-sm text-gray-500">Limit: ${category.limit.toFixed(2).replace('.', ',')}€</p>
                </div>
            </div>
            <div class="flex space-x-2">
                <button type="button" onclick="editCategory(${category.id})" 
                    class="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                    </svg>
                </button>
                <button type="button" onclick="deleteCategory(${category.id})" 
                    class="p-2 text-red-600 hover:bg-red-50 rounded-lg transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                    </svg>
                </button>
            </div>
        `;
        container.appendChild(div);
    });
}

