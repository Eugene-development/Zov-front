<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';

	let { showModal = $bindable(false), conditions = [] } = $props<{
		showModal: boolean;
		conditions: string[];
	}>();
</script>

<Modal bind:showModal title="Условия акции">
	{#if conditions && conditions.length > 0}
		<div class="flex flex-col gap-4 text-secondary">
			<ul class="list-none space-y-3">
				{#each conditions as condition}
					<li class="flex items-start gap-3">
						<svg
							class="mt-1 h-4 w-4 shrink-0 text-accent"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="2"
						>
							<path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
						</svg>
						<span class="text-sm leading-relaxed">{@html condition}</span>
					</li>
				{/each}
			</ul>
		</div>
	{:else}
		<div class="flex flex-col gap-4 text-secondary">
			<p class="text-sm">Подробные условия акции уточняйте у наших дизайнеров.</p>
		</div>
	{/if}
</Modal>
