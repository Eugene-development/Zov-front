<script>
	import { onMount } from 'svelte';

	let heroVisible = $state(false);
	let sections = $state({});

	onMount(() => {
		heroVisible = true;

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						sections[entry.target.id] = true;
					}
				});
			},
			{ threshold: 0.15, rootMargin: '0px 0px -50px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	const facades = [
		{
			id: 'enamel',
			title: 'Эмаль (Крашеный МДФ)',
			description:
				'Гладкие матовые или глянцевые поверхности любого оттенка. Эмаль наносится в несколько слоев, что создает идеальное покрытие без швов по кромке. Идеально для современных, минималистичных и неоклассических интерьеров.',
			image: '/images/facade_enamel.png',
			details: {
				base: 'Плита МДФ',
				coating: 'Многослойная эмаль (матовая / глянцевая)',
				thickness: '19 мм',
				minSize: '100 × 100 мм',
				maxSize: '2750 × 1100 мм'
			}
		},
		{
			id: 'wood',
			title: 'Массив дерева',
			description:
				'Классика, которая никогда не выходит из моды. Натуральная текстура дуба или ясеня привносит в дом тепло и уют. Фасады из массива поддаются реставрации и с годами становятся только благороднее.',
			image: '/images/facade_wood.png',
			details: {
				base: 'Массив ясеня / дуба',
				coating: 'Эмаль, масловоск, воскобейц, патина',
				thickness: '21 мм',
				minSize: '140 × 140 мм',
				maxSize: '2400 × 900 мм'
			}
		},
		{
			id: 'hpl',
			title: 'Пластики',
			description:
				'Максимально устойчивые к царапинам, ударам и температурам материал. Пластики идеально имитируют текстуры бетона, камня или дерева, сохраняя при этом индустриальную строгость и премиальный вид.',
			image: '/images/facade_hpl.png',
			details: {
				base: 'Плита МДФ',
				coating: 'Декоративный пластик',
				thickness: '18 мм / 21 мм',
				minSize: '100 × 100 мм',
				maxSize: '2800 × 1300 мм'
			}
		},
		{
			id: 'acrylic',
			title: 'Акрил',
			description:
				'Идеально ровная, зеркальная глянцевая или бархатистая матовая (супермат) поверхность. Фасады из акрила обладают высокой ударопрочностью, не выцветают на солнце и придают интерьеру премиальный блеск.',
			image: '/images/facade_acrylic.png',
			details: {
				base: 'Плита МДФ',
				coating: 'Акриловый пластик',
				thickness: '19 мм',
				minSize: '100 × 100 мм',
				maxSize: '2800 × 1300 мм'
			}
		}
	];
</script>

<svelte:head>
	<title>Фасады для кухни | Эмаль, Массив, Пластик, Акрил | ЗОВ</title>
	<meta
		name="description"
		content="Каталог мебельных фасадов премиум-класса от фабрики ЗОВ. Выберите материал основы и покрытия для вашей идеальной кухни."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[80vh] overflow-hidden bg-surface" id="hero">
	<div class="absolute inset-0">
		<img
			src="/images/facades_hero.png"
			alt="Мебельные фасады"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<div
			class="absolute inset-0 bg-gradient-to-r from-primary/95 via-primary/70 to-primary/30"
		></div>
	</div>

	<div class="relative z-10 flex min-h-[80vh] items-center">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-2xl">
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span
						class="inline-flex items-center gap-2 border border-white/20 bg-white/5 px-4 py-2 text-[11px] tracking-[0.25em] text-white/70 uppercase backdrop-blur-sm"
					>
						Материалы
					</span>
				</div>

				<h1
					class="text-5xl leading-[1.1] font-light text-white opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Фасад это лицо
					<br />
					вашей кухни
				</h1>

				<p
					class="mt-8 max-w-xl text-base leading-relaxed text-white/70 opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Фасады задают характер вашего домашнего интерьера. От натурального массива до
					технологичного акрила: мы предлагаем материалы, которые сочетают в себе безупречную
					эстетику, функциональность и долговечность.
				</p>
			</div>
		</div>
	</div>
</section>

<!-- ==================== FACADES SHOWCASE ==================== -->
<section class="relative bg-surface py-section" id="facades-catalog" data-animate>
	<div class="mx-auto max-w-7xl px-6">
		<div class="mb-16 opacity-0 lg:mb-24" class:animate-fade-up={sections['facades-catalog']}>
			<h2
				class="text-4xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Коллекция <span class="text-secondary">фасадов</span>
			</h2>
		</div>

		<div class="flex flex-col gap-20 lg:gap-32">
			{#each facades as facade, index}
				<div
					class="grid items-center gap-12 lg:grid-cols-2 lg:gap-20"
					id={`facade-${facade.id}`}
					data-animate
				>
					<!-- Image Side -->
					<div
						class="relative aspect-[4/3] overflow-hidden opacity-0 lg:aspect-[4/5] {index % 2 !== 0
							? 'lg:order-last'
							: ''}"
						class:animate-fade-up={sections[`facade-${facade.id}`]}
						style="animation-delay: 0.2s"
					>
						<img
							src={facade.image}
							alt={facade.title}
							class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
						/>
						<div
							class="absolute inset-0 bg-gradient-to-t from-primary/50 to-transparent lg:hidden"
						></div>
					</div>

					<!-- Content Side -->
					<div
						class="flex flex-col opacity-0"
						class:animate-fade-up={sections[`facade-${facade.id}`]}
						style="animation-delay: 0.4s"
					>
						<h3
							class="text-3xl font-light text-primary lg:text-4xl"
							style="font-family: var(--font-heading);"
						>
							{facade.title}
						</h3>
						<p class="mt-6 text-base leading-relaxed text-text-secondary">
							{facade.description}
						</p>

						<!-- Specifications Table -->
						<div class="mt-10 border-t border-border-light pt-6">
							<dl class="flex flex-col gap-4">
								<div class="flex items-center justify-between border-b border-border-light/50 pb-4">
									<dt class="text-xs tracking-wider text-text-muted uppercase">Материал основы</dt>
									<dd class="text-right text-sm font-medium text-primary">{facade.details.base}</dd>
								</div>
								<div class="flex items-center justify-between border-b border-border-light/50 pb-4">
									<dt class="text-xs tracking-wider text-text-muted uppercase">Покрытие</dt>
									<dd class="text-right text-sm font-medium text-primary">
										{facade.details.coating}
									</dd>
								</div>
								<div class="flex items-center justify-between border-b border-border-light/50 pb-4">
									<dt class="text-xs tracking-wider text-text-muted uppercase">Толщина</dt>
									<dd class="text-right text-sm font-medium text-primary">
										{facade.details.thickness}
									</dd>
								</div>
								<div class="flex items-start justify-between pb-2">
									<dt class="mt-0.5 text-xs tracking-wider text-text-muted uppercase">
										Размеры <span class="text-[10px] opacity-70">(мин / макс)</span>
									</dt>
									<dd class="text-right text-sm font-medium text-primary">
										{facade.details.minSize} <br />
										<span class="mx-1 text-xs text-text-muted">—</span> <br class="sm:hidden" />
										{facade.details.maxSize}
									</dd>
								</div>
							</dl>
						</div>

						<div class="mt-10">
							<a
								href="/call-designer"
								class="group inline-flex items-center gap-3 border border-border-medium px-8 py-4 text-xs tracking-[0.15em] text-primary uppercase transition-all duration-300 hover:border-secondary hover:text-secondary"
							>
								Заказать с этим фасадом
								<svg
									class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
									stroke-width="1.5"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
									/>
								</svg>
							</a>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-surface-warm py-section-sm lg:py-section"
	id="cta-section"
	data-animate
>
	<div class="relative mx-auto max-w-4xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['cta-section']}>
			<span class="text-[11px] tracking-[0.3em] text-secondary uppercase">Образцы</span>
			<h2
				class="mt-4 text-3xl font-light text-primary lg:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Посмотрите вживую
			</h2>
			<p class="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-text-secondary">
				Ни одна фотография не передаст тактильных ощущений от текстурного пластика, прохлады
				глубокого глянца или теплоты натурального дерева. Посетите салон фабрики, чтобы прикоснуться
				к образцам.
			</p>
			<div class="mt-10 flex justify-center">
				<a
					href="/showrooms"
					class="group inline-flex items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
				>
					Адреса салонов
				</a>
			</div>
		</div>
	</div>
</section>
