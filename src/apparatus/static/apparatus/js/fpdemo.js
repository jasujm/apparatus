(function($) {
    function roundPreservingSum(numbers) {
        const sum = (x, y) => x + y;
        const sum_of_numbers_before_floor = Math.round(numbers.reduce(sum));
        var decimals = [];
        for (var i = 0; i < numbers.length; ++i) {
            const number_floored = Math.floor(numbers[i]);
            decimals.push({ decimal: numbers[i] - number_floored, index: i });
            numbers[i] = number_floored;
        }
        decimals.sort(d => d.decimal);
        const sum_of_numbers_after_floor = numbers.reduce(sum);
        for (i = sum_of_numbers_before_floor - sum_of_numbers_after_floor; i > 0; --i) {
            const d = decimals.pop();
            ++numbers[d.index];
        }
        return numbers;
    }
    function roundedPercentage(p, precision) {
        if (precision) {
            return `${(100.0 * p).toPrecision(precision)}&nbsp%`;
        } else {
            return `${Math.round(100.0 * p)}&nbsp%`;
        }
    }
    $.fn.extend({
        fpdemo: function(prevalence, sensitivity, specificity) {
            const grid_dimension = Math.floor(this.outerWidth() / 30);
            const population_size = grid_dimension * grid_dimension;
            const n_positives = population_size * prevalence;
            const n_true_positives = n_positives * sensitivity;
            const n_false_negatives = n_positives - n_true_positives;
            const n_negatives = population_size - n_positives;
            const n_true_negatives = n_negatives * specificity;
            const n_false_positives = n_negatives - n_true_negatives;
            const bins = roundPreservingSum(
                [
                    n_true_negatives,
                    n_false_positives,
                    n_true_positives,
                    n_false_negatives,
                ]
            );
            const types = [
                { class: "negative", symbol: "&nbsp;" },
                { class: "negative", symbol: '<i class="fas fa-exclamation-triangle"></i>' },
                { class: "positive", symbol: '<i class="fas fa-check-circle"></i>' },
                { class: "positive", symbol: "&nbsp;" },
            ];
            var thresholds = [];
            var partial_sum = 0;
            for (var i = 0; i < bins.length; ++i) {
                partial_sum += bins[i];
                thresholds.push(partial_sum);
            }
            var type_index = 0;
            this.empty().addClass("population");
            for (i = 0; i < population_size; ++i) {
                if (i > thresholds[0]) {
                    ++type_index;
                    thresholds.shift();
                }
                const box = $("<div></div>")
                      .addClass("box")
                      .addClass(types[type_index].class).html(types[type_index].symbol);
                this.append(box);
            }
            $(".fpdemo-population-size").text(population_size);
            $(".fpdemo-sensitivity").html(roundedPercentage(sensitivity, 3));
            $(".fpdemo-specificity").html(roundedPercentage(specificity, 3));
            $(".fpdemo-false-positives").text(bins[1]);
            $(".fpdemo-true-positives").text(bins[2]);
            $(".fpdemo-positives").text(bins[1] + bins[2]);
            $(".fpdemo-prevalence").html(roundedPercentage(prevalence));
            $(".fpdemo-fdr").html(
                roundedPercentage(n_false_positives / (n_false_positives + n_true_positives), 3)
            );
            return this;
        }
    });
})(jQuery);
