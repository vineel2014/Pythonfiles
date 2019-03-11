import gc
gc_was_enabled = gc.isenabled()

if gc_was_enabled:
    
    print("Garbage Collector was enabled:",gc_was_enabled)

    gc.collect()




