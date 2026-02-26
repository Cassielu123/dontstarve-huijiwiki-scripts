from json.encoder import JSONEncoder

from luaparser import astnodes


class SkillTreeEncoder(JSONEncoder):
    def default(self, o):
        if (not isinstance(o, astnodes.Node)) and hasattr(o, "to_json"):
            # print("to json for", o)
            return o.to_json()
        elif type(o) in (
            astnodes.Function,
            astnodes.AnonymousFunction,
            astnodes.LocalFunction,
        ):
            # print("to json for", o)
            return True
        return super().default(o)
