"""
>>> hydra.initialize(config_path='{{cookiecutter.project_slug}}/conf', version_base="1.3")
>>> cfg = hydra.compose(config_name='config')
"""
import hydra
import omegaconf

import {{cookiecutter.project_slug}}.constants
import {{cookiecutter.project_slug}}.callbacks

constants = {{cookiecutter.project_slug}}.constants.Constants()


@hydra.main(config_path="conf", config_name="config", version_base="1.3")
def main(cfg):
    train_dl = hydra.utils.instantiate(cfg.data.train)
    optim = hydra.utils.instantiate(cfg.model.optimizer)
    try:
        scheduler = hydra.utils.instantiate(cfg.model.scheduler)
    except omegaconf.errors.ConfigAttributeError:
        scheduler = None
    model = hydra.utils.instantiate(cfg.model.nn, optim=optim, scheduler=scheduler)
    callbacks = {{cookiecutter.project_slug}}.callbacks.instantiate_callbacks(cfg.callbacks)
    trainer = hydra.utils.instantiate(cfg.trainer, callbacks=callbacks)
    trainer.fit(model=model, train_dataloaders=train_dl)
    trainer.checkpoint_callback.to_yaml()


if __name__ == "__main__":
    main()
