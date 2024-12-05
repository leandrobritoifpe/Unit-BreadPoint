document.addEventListener('DOMContentLoaded', function() {
    const dayButtons = document.querySelectorAll('.day-btn');

    dayButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.classList.toggle('selected');
            updateTotalDisplay();
        });
    });

    document.querySelectorAll('.month-btn').forEach(button => {
        button.addEventListener('click', event => {
            const selectedButton = event.target;
            const buttons = document.querySelectorAll('.month-btn');
            buttons.forEach(button => button.classList.remove('selected'));
            selectedButton.classList.add('selected');
            updateTotalDisplay();
        });
    });

    // Função para calcular o valor total
    function calculateTotal() {
        let total = 0;

        // Verifica os planos selecionados
        const selectedPlans = document.querySelectorAll('.btRadioPlan:checked');
        selectedPlans.forEach(function(plan) {
            const planValue = plan.value;
            if (planValue === 'wellness') {
                total += 10;
            } else if (planValue === 'familyFriend') {
                total += 15;
            } else if (planValue === 'fastEasy') {
                total += 20;
            } else if (planValue === 'chefFavorite') {
                total += 25;
            } else if (planValue === 'veggies') {
                total += 30;
            }
        });

        // Verifica os planos selecionados de planOne
        const selectedPlanOne = document.querySelectorAll('input[name="planOne"]:checked');
        selectedPlanOne.forEach(function(plan) {
            const planValue = plan.value;
            if (planValue === 'basic') {
                total += 5;
            } else if (planValue === 'family-friendly') {
                total += 10;
            }
        });

        // Verifica as opções de refeições por semana
        const selectedServings = document.querySelector('.month-btn.selected');
        if (selectedServings) {
            const servingsValue = parseInt(selectedServings.value, 10);
            total += servingsValue * 5; // Multiplica o valor por 5 (valor fictício)
        }

        // Verifica as opções de refeições por semana
        const selectedMeals = document.querySelectorAll('.day-btn.selected');
        selectedMeals.forEach(function(meal) {
            const mealValue = parseInt(meal.value, 10);
            total += mealValue * 3; // Multiplica o valor por 3 (valor fictício)
        });

        return total;
    }

    // Função para atualizar o valor final na div
    function updateTotalDisplay() {
        const total = calculateTotal();
        const totalDisplay = document.querySelector('.div-finish-select-plan');
        totalDisplay.textContent = `Total: $${total.toFixed(2)}`;
    }

    // Adiciona eventos de clique aos botões de plano
    const planButtons = document.querySelectorAll('.btRadioPlan');
    planButtons.forEach(function(button) {
        button.addEventListener('click', updateTotalDisplay);
    });

    // Adiciona eventos de clique aos botões de planOne
    const planOneButtons = document.querySelectorAll('input[name="planOne"]');
    planOneButtons.forEach(function(button) {
        button.addEventListener('click', updateTotalDisplay);
    });
});