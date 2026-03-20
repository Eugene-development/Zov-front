<script>
	import { fade, fly } from 'svelte/transition';
	import { onMount } from 'svelte';

	let isVisible = $state(false);

	onMount(() => {
		isVisible = true;
	});

	const features = [
		{ title: 'Точные замеры', desc: 'Лазерное 3D-сканирование помещения для идеального встраивания.', colSpan: 'col-span-1 md:col-span-2' },
		{ title: 'Премиум фурнитура', desc: 'Бесшумное скольжение и доводчики от ведущих брендов.', colSpan: 'col-span-1 md:col-span-1' },
		{ title: 'Надежные материалы', desc: 'Экологичные плиты европейского стандарта с высокой плотностью.', colSpan: 'col-span-1 md:col-span-1' },
		{ title: 'Сложная архитектура', desc: 'Проектируем наполнение, учитывая ваш гардероб и обувь до мелочей.', colSpan: 'col-span-1 md:col-span-2' },
	];
</script>

<svelte:head>
	<title>Шкафы и гардеробные | ЗОВ</title>
	<meta name="description" content="Премиальные шкафы и гардеробные системы фабрики ЗОВ. Индивидуальные проекты, идеальная геометрия и долговечность." />
</svelte:head>

<main class="bg-surface-warm min-h-screen">
	<!-- Hero: Split Layout -->
	<section class="grid lg:grid-cols-2 min-h-[70vh]">
		<div class="flex flex-col justify-center px-8 lg:px-20 py-16 bg-white shrink-0">
			{#if isVisible}
				<div in:fly={{ x: -30, duration: 1000, delay: 100 }}>
					<span class="text-sm font-medium uppercase tracking-[0.3em] text-accent mb-6 block">Системы хранения</span>
					<h1 class="text-4xl lg:text-6xl font-light tracking-wide text-primary mb-8 leading-tight" style="font-family: var(--font-heading);">
						Идеальный порядок 
						<br />
						<span class="text-secondary">в каждой детали</span>
					</h1>
					<p class="text-lg text-secondary leading-relaxed max-w-lg mb-12">
						Мы создаем уникальные встроенные и корпусные шкафы, которые становятся органичным продолжением вашей квартиры. Максимальная вместимость и премиальная эстетика.
					</p>
					<a href="/showrooms" class="inline-flex items-center gap-2 bg-primary text-white hover:bg-secondary px-8 py-4 rounded-full transition-colors duration-300 tracking-wider text-sm">
						Спроектировать шкаф
						<svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/>
						</svg>
					</a>
				</div>
			{/if}
		</div>
		<div class="relative bg-border-light hidden lg:block overflow-hidden">
			<!-- Hero Placeholder Diagram inside -->
			<div class="absolute inset-0 flex flex-col items-center justify-center text-primary/30">
				<svg class="w-32 h-32 mb-6 opacity-30" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v14a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 12h16M12 4v16"/>
				</svg>
				<span class="text-sm uppercase tracking-[0.2em] font-medium">Заглушка: Большое фото роскошного шкафа</span>
			</div>
		</div>
	</section>

	<!-- Bento Box Features (Difference in structure from Kitchens) -->
	<section class="py-24 px-6 max-w-7xl mx-auto">
		<div class="text-center mb-16">
			<h2 class="text-3xl lg:text-4xl font-light tracking-wide text-primary" style="font-family: var(--font-heading);">
				Безупречное качество от замера до установки
			</h2>
		</div>

		<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
			{#each features as feature, i}
				<div class="bg-white p-10 rounded-3xl shadow-soft hover:shadow-elevated transition-shadow duration-300 flex flex-col justify-end min-h-[250px] relative overflow-hidden {feature.colSpan}">
					<div class="absolute top-8 right-8 text-6xl font-light text-border-medium/30 transition-colors duration-500 group-hover:text-border-medium/60" style="font-family: var(--font-heading);">
						0{i+1}
					</div>
					<h3 class="text-2xl font-light text-primary mb-3" style="font-family: var(--font-heading);">{feature.title}</h3>
					<p class="text-secondary leading-relaxed">{feature.desc}</p>
				</div>
			{/each}
		</div>
	</section>

	<!-- Types of Wardrobes: Horizontal/Masonry visual approach -->
	<section class="py-24 px-6 bg-white overflow-hidden">
		<div class="max-w-7xl mx-auto">
			<div class="flex flex-col lg:flex-row justify-between items-end mb-16 gap-8">
				<div class="max-w-2xl">
					<span class="text-sm font-medium uppercase tracking-[0.2em] text-accent mb-4 block">Варианты решений</span>
					<h2 class="text-3xl lg:text-4xl font-light tracking-wide text-primary" style="font-family: var(--font-heading);">
						Виды систем
					</h2>
				</div>
			</div>

			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
				
				<!-- Card 1 -->
				<div class="group cursor-pointer">
					<div class="aspect-[3/4] rounded-2xl bg-[#F0F0F0] mb-6 flex items-center justify-center relative overflow-hidden transition-all duration-500 group-hover:bg-[#E5E5E5]">
						<div class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-primary/10 to-transparent"></div>
						<span class="text-xs uppercase tracking-[0.2em] font-medium text-primary/40 relative z-10">Заглушка: Встроенный шкаф</span>
					</div>
					<h3 class="text-xl font-light tracking-wide text-primary mb-2" style="font-family: var(--font-heading);">Встроенные шкафы</h3>
					<p class="text-secondary text-sm leading-relaxed">Монтируются напрямую от пола до потолка, скрывая неровности стен и максимально эффективно используя ниши.</p>
				</div>

				<!-- Card 2 -->
				<div class="group cursor-pointer lg:-translate-y-8">
					<div class="aspect-[3/4] rounded-2xl bg-[#E8E8E8] mb-6 flex items-center justify-center relative overflow-hidden transition-all duration-500 group-hover:bg-[#DDDDDD]">
						<div class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-primary/10 to-transparent"></div>
						<span class="text-xs uppercase tracking-[0.2em] font-medium text-primary/40 relative z-10">Заглушка: Корпусный шкаф</span>
					</div>
					<h3 class="text-xl font-light tracking-wide text-primary mb-2" style="font-family: var(--font-heading);">Корпусные решения</h3>
					<p class="text-secondary text-sm leading-relaxed">Самостоятельные модули, которые можно перемещать. Акцентные фасады и витринные стеклянные элементы.</p>
				</div>

				<!-- Card 3 -->
				<div class="group cursor-pointer lg:-translate-y-16">
					<div class="aspect-[3/4] rounded-2xl bg-[#F0F0F0] mb-6 flex items-center justify-center relative overflow-hidden transition-all duration-500 group-hover:bg-[#E5E5E5]">
						<div class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-primary/10 to-transparent"></div>
						<span class="text-xs uppercase tracking-[0.2em] font-medium text-primary/40 relative z-10">Заглушка: Гардеробная</span>
					</div>
					<h3 class="text-xl font-light tracking-wide text-primary mb-2" style="font-family: var(--font-heading);">Гардеробные комнаты</h3>
					<p class="text-secondary text-sm leading-relaxed">Открытые и закрытые модульные системы премиум-класса с умной подсветкой и организаторами.</p>
				</div>

			</div>
		</div>
	</section>

	<!-- Minimal Footer CTA -->
	<section class="border-t border-border-light px-6 py-24 bg-surface-warm">
		<div class="max-w-4xl mx-auto text-center">
			<h2 class="text-3xl lg:text-5xl font-light tracking-wide text-primary mb-8" style="font-family: var(--font-heading);">
				Закажите расчет стоимости
			</h2>
			<a href="/showrooms" class="inline-block relative group">
				<span class="relative z-10 text-lg tracking-widest text-primary uppercase font-medium">Связаться с дизайнером</span>
				<span class="absolute bottom-0 left-0 w-full h-px bg-primary transform scale-x-0 origin-left transition-transform duration-500 ease-out group-hover:scale-x-100"></span>
			</a>
		</div>
	</section>
</main>
